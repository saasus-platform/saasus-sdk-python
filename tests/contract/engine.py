"""Round-trips the generated SDK clients against a Prism mock of the spec.

Requests the SDK builds must be accepted by the mock and responses must
deserialize into the SDK types. Operations are enumerated from the spec at run
time, so an SDK missing one simply has no case -- which lets the same suite run
against a previously released SDK (forward compatibility, test (C)).

Only ``<operation>_with_http_info`` is exercised: the plain form just unwraps
``ApiResponse.data`` and ``async_req`` reuses the same ``call_api``, so neither
adds deserialization logic, and only this form exposes the HTTP status.

Synthetic data only: a constant bearer token and request values from the spec;
no response body, token or PII is logged.
"""

from __future__ import annotations

import importlib
import inspect
import os
import re
from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional, get_args

from spec import Operation, Spec

# The mock requires a bearer credential but does not validate its value, and
# this suite verifies the generated client against the spec, not the
# authentication layer, so a constant placeholder is enough.
SYNTHETIC_TOKEN = "synthetic-bearer-token"

_PACKAGE = "saasus_sdk_python.src"
_WITH_HTTP_INFO = "_with_http_info"


class ContractFailure(AssertionError):
    """A contract violation phrased without any response body, token or PII."""


@dataclass
class _Module:
    name: str
    spec: Spec
    methods: Dict[str, Callable[..., Any]]  # normalized method base name -> bound method
    api_exception: Optional[type]  # None when the SDK has no such module (no method, so no case)


@dataclass
class Case:
    module: str
    operation_id: str
    variant_index: int
    label: str
    method: Callable[..., Any]
    spec: Spec
    op: Operation
    api_exception: type

    @property
    def id(self) -> str:
        base = f"{self.module}.{self.operation_id}"
        return f"{base}({self.label})" if self.label else base

    def run(self) -> None:
        round_trip(self)


# --- configuration ----------------------------------------------------------


def spec_dir() -> Optional[str]:
    return os.getenv("CONTRACT_SPEC_DIR") or None


def configured_modules() -> List[str]:
    return os.getenv("CONTRACT_MODULES", "").split()


def require_complete() -> bool:
    return os.getenv("CONTRACT_REQUIRE_COMPLETE", "").lower() == "true"


def prism_url(module: str) -> Optional[str]:
    return os.getenv("PRISM_URL_" + module.upper()) or None


def generated_modules() -> List[str]:
    """Module directories generated into the SDK (those with an api_client)."""
    package = importlib.import_module(_PACKAGE)
    # ``saasus_sdk_python.src`` ships no __init__.py, so it is a namespace
    # package whose __file__ is None; its directory comes from __path__.
    src = next(iter(package.__path__))
    return sorted(
        entry
        for entry in os.listdir(src)
        if os.path.isfile(os.path.join(src, entry, "api_client.py"))
    )


# --- client wiring ----------------------------------------------------------


def _load_module(name: str, directory: str, base_url: str) -> _Module:
    spec = Spec.load(directory, name)
    if name not in generated_modules():
        # A released SDK may lack a module the current spec carries: keep its
        # spec with no method so it yields no case, while unmapped_operations
        # still reports its operations and (B) fails rather than silently
        # dropping the module. Any other import error propagates.
        return _Module(name=name, spec=spec, methods={}, api_exception=None)
    api_pkg = importlib.import_module(f"{_PACKAGE}.{name}.api")
    api_client_cls = importlib.import_module(f"{_PACKAGE}.{name}.api_client").ApiClient
    configuration_cls = importlib.import_module(f"{_PACKAGE}.{name}.configuration").Configuration
    api_exception = importlib.import_module(f"{_PACKAGE}.{name}.exceptions").ApiException

    configuration = configuration_cls()
    configuration.host = base_url
    configuration.access_token = SYNTHETIC_TOKEN
    client = api_client_cls(configuration)

    # A module's operations are spread across several *Api classes; collect the
    # with_http_info method from each.
    methods: Dict[str, Callable[..., Any]] = {}
    for attribute in vars(api_pkg).values():
        if not (inspect.isclass(attribute) and attribute.__name__.endswith("Api")):
            continue
        instance = attribute(client)
        for method_name, bound in inspect.getmembers(instance, inspect.ismethod):
            if method_name.endswith(_WITH_HTTP_INFO):
                methods[_normalize(method_name[: -len(_WITH_HTTP_INFO)])] = bound
    return _Module(name=name, spec=spec, methods=methods, api_exception=api_exception)


_modules_cache: Optional[List[_Module]] = None


def _modules() -> List[_Module]:
    global _modules_cache
    if _modules_cache is None:
        directory = spec_dir()
        loaded: List[_Module] = []
        if directory:
            for name in configured_modules():
                base_url = prism_url(name)
                if not base_url:
                    continue  # no mock -> contributes no case
                loaded.append(_load_module(name, directory, base_url))
        _modules_cache = loaded
    return _modules_cache


# --- enumeration ------------------------------------------------------------


def build_cases() -> List[Case]:
    cases: List[Case] = []
    for module in _modules():
        for op_id in sorted(module.spec.ops):
            method = module.methods.get(_normalize(op_id))
            if method is None:
                continue  # unmapped; reported by unmapped_operations for (B)
            op = module.spec.ops[op_id]
            labels = module.spec.body_variant_labels(op) or [""]
            for index, label in enumerate(labels):
                cases.append(
                    Case(
                        module=module.name,
                        operation_id=op_id,
                        variant_index=index,
                        label=label,
                        method=method,
                        spec=module.spec,
                        op=op,
                        api_exception=module.api_exception,
                    )
                )
    return cases


def unmapped_operations() -> List[str]:
    """Spec operations with no matching generated method, per configured module."""
    missing: List[str] = []
    for module in _modules():
        for op_id in sorted(module.spec.ops):
            if _normalize(op_id) not in module.methods:
                missing.append(f"{module.name}.{op_id}")
    return missing


# --- round trip -------------------------------------------------------------


def round_trip(case: Case) -> None:
    kwargs = build_kwargs(case.method, case.spec, case.op, case.variant_index)
    try:
        response = case.method(**kwargs)
    except case.api_exception as error:
        status = getattr(error, "status", None)
        # An operation with no declared success must surface one of its declared
        # errors; anything else is a contract break.
        if case.op.has_success or status not in case.op.statuses:
            raise ContractFailure(f"{case.id}: unexpected status {status}") from None
        return
    except Exception as error:  # noqa: BLE001
        # Deserialization and request-side validation failures land here. The
        # generated models put the response body in the message, so report only
        # the exception type, never the body.
        raise ContractFailure(f"{case.id}: round trip failed ({type(error).__name__})") from None

    status = getattr(response, "status_code", None)
    if _returns_body(case.method) and getattr(response, "data", None) is None:
        raise ContractFailure(f"{case.id}: status {status}: response was not deserialized into the SDK type")


def _returns_body(with_http_info: Callable[..., Any]) -> bool:
    """Whether the SDK method is contracted to deserialize a response body.

    Keyed on the SDK's own return type, not the latest spec: a body the current
    spec adds to an operation a released SDK still ignores (its plain method
    returns ``None``) is a backward-compatible addition, not a forward-compat
    break (C). The plain ``<operation>`` method that ``_with_http_info`` unwraps
    carries that return type.
    """
    plain = getattr(with_http_info.__self__, with_http_info.__name__[: -len(_WITH_HTTP_INFO)])
    return inspect.signature(plain).return_annotation is not None


def build_kwargs(method: Callable[..., Any], spec: Spec, op: Operation, variant_index: int) -> Dict[str, Any]:
    """Bind the generated method's arguments by name.

    Generated path/query/header arguments carry the spec parameter name in
    snake_case (``X-Saasus-Referer`` -> ``x_saasus_referer``), except a name
    colliding with a Python builtin/keyword, which the generator prefixes with
    ``var_`` (``date`` -> ``var_date``). Binding by normalized name rather than
    position keeps each value on the right argument even for an SDK generated
    from a different spec revision. An argument the spec cannot explain fails
    explicitly, since position binding would send the wrong value.
    """
    named = [
        parameter
        for parameter in inspect.signature(method).parameters.values()
        if parameter.kind in (inspect.Parameter.POSITIONAL_OR_KEYWORD, inspect.Parameter.KEYWORD_ONLY)
        and parameter.name != "self"
    ]

    values_by_name: Dict[str, Any] = {_normalize(name): value for name, value in spec.params_values(op).items()}
    for path_param in op.path_params:
        name = path_param.get("name")
        if isinstance(name, str):
            values_by_name[_normalize(name)] = spec.param_value(path_param)

    kwargs: Dict[str, Any] = {}
    unexplained: List[inspect.Parameter] = []
    for parameter in named:
        key = _normalize(parameter.name)
        if key not in values_by_name and parameter.name.startswith("var_"):
            # Recover the spec name behind a ``var_``-prefixed argument (the
            # generator's escape for a Python builtin/keyword).
            key = _normalize(parameter.name[len("var_") :])
        if key in values_by_name:
            # A spec value with no matching argument stays in the map: an SDK
            # predating that parameter simply never receives it.
            kwargs[parameter.name] = values_by_name.pop(key)
        else:
            unexplained.append(parameter)

    if op.body_schema is not None:
        if len(unexplained) == 1:
            body = unexplained.pop()
            value = spec.body_value(op, variant_index)
            try:
                kwargs[body.name] = _body_argument(body.annotation, value)
            except Exception as error:  # noqa: BLE001
                # The conversion puts the body in its message; report the type
                # name only.
                raise ContractFailure(
                    f"{op.id}: the spec request body does not fit the SDK model ({type(error).__name__})"
                ) from None
        elif not unexplained:
            raise ContractFailure(f"{op.id}: the SDK method has no argument for the request body the spec declares")
    if unexplained:
        raise ContractFailure(f"{op.id}: arguments not explained by the spec: {[p.name for p in unexplained]}")

    return kwargs


def _body_argument(annotation: Any, value: Any) -> Any:
    """Convert a spec-derived request body into the model the argument declares.

    A oneOf body is a holder whose ``actual_instance`` only ``from_dict`` sets,
    so passing the synthesized dict straight through serializes to ``null`` or
    fails. ``from_dict`` is the SDK's own conversion, reused here. An argument
    not modelled as such a class (an array or free-form object) is passed
    through for the generated method to convert.
    """
    if isinstance(value, dict):
        for candidate in (annotation, *get_args(annotation)):
            from_dict = getattr(candidate, "from_dict", None)
            if callable(from_dict):
                return from_dict(value)
    return value


def _normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower())
