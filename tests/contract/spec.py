"""Parsed OpenAPI document: the source of the request inputs.

Values come from the spec rather than being hardcoded, so they are acceptable
by construction -- the Prism mock validates requests against the same document.
It also keeps the approach language-independent: the only language-specific
part (binding an operationId to a generated method) lives in ``engine.py``.

This is a port of the Go harness' ``spec_test.go`` so the synthesis rules stay
identical across the SDK implementations.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

import yaml

SYNTHETIC_VALUE = "synthetic"

_HTTP_METHODS = ("get", "put", "post", "delete", "patch", "head", "options")
_PATH_PARAM_RE = re.compile(r"\{([^}]+)\}")


@dataclass
class Operation:
    id: str
    # Ordered as they appear in the path template, which is the order the
    # generated method takes them in.
    path_params: List[Dict[str, Any]] = field(default_factory=list)
    # Query and header parameters together: the generated method takes each as
    # its own named argument, bound by name in engine.build_kwargs.
    params: List[Dict[str, Any]] = field(default_factory=list)
    body_schema: Optional[Dict[str, Any]] = None
    statuses: set = field(default_factory=set)
    # 2xx statuses that declare an application/json body; the response for one
    # of these must deserialize into a non-null payload.
    json_statuses: set = field(default_factory=set)
    has_success: bool = False


class Spec:
    def __init__(self, root: Dict[str, Any]):
        self.root = root
        self.ops: Dict[str, Operation] = {}
        self._index()

    # --- loading ------------------------------------------------------------

    @classmethod
    def load(cls, directory: str, module: str) -> "Spec":
        with open(os.path.join(directory, module + ".yml"), encoding="utf-8") as handle:
            decoded = yaml.safe_load(handle)
        root = _stringify_keys(decoded)
        if not isinstance(root, dict):
            raise ValueError(f"{module}: not an OpenAPI document")
        return cls(root)

    # --- indexing -----------------------------------------------------------

    def _index(self) -> None:
        paths = self.root.get("paths")
        if not isinstance(paths, dict):
            return
        for path, raw_item in paths.items():
            if not isinstance(raw_item, dict):
                continue
            for method in _HTTP_METHODS:
                raw_op = raw_item.get(method)
                if not isinstance(raw_op, dict):
                    continue
                op_id = raw_op.get("operationId")
                if not isinstance(op_id, str):
                    continue
                op = Operation(id=op_id)
                self._load_params(op, path, raw_item, raw_op)
                op.body_schema = self._body_schema(raw_op)
                self._load_statuses(op, raw_op)
                self.ops[op_id] = op

    def _load_params(self, op: Operation, path: str, path_item: Dict[str, Any], raw_op: Dict[str, Any]) -> None:
        # Path-level parameters apply to every operation of the path item.
        by_name: Dict[str, Dict[str, Any]] = {}
        for raw_list in (path_item.get("parameters"), raw_op.get("parameters")):
            if not isinstance(raw_list, list):
                continue
            for raw in raw_list:
                if not isinstance(raw, dict):
                    continue
                param = self._resolve(raw)
                name = param.get("name")
                location = param.get("in")
                if location == "path" and isinstance(name, str):
                    by_name[name] = param
                elif location in ("query", "header"):
                    op.params.append(param)
        for match in _PATH_PARAM_RE.findall(path):
            if match in by_name:
                op.path_params.append(by_name[match])

    def _body_schema(self, raw_op: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        body = raw_op.get("requestBody")
        if not isinstance(body, dict):
            return None
        content = self._resolve(body).get("content")
        if not isinstance(content, dict):
            return None
        json_content = content.get("application/json")
        if not isinstance(json_content, dict):
            return None
        schema = json_content.get("schema")
        if not isinstance(schema, dict):
            return None
        return self._resolve(schema)

    def _load_statuses(self, op: Operation, raw_op: Dict[str, Any]) -> None:
        responses = raw_op.get("responses")
        if not isinstance(responses, dict):
            return
        for key, raw_response in responses.items():
            try:
                code = int(key)
            except (TypeError, ValueError):
                continue  # "default" and the like carry no status
            op.statuses.add(code)
            if 200 <= code < 300:
                op.has_success = True
                if self._declares_json_body(raw_response):
                    op.json_statuses.add(code)

    def _declares_json_body(self, raw_response: Any) -> bool:
        if not isinstance(raw_response, dict):
            return False
        content = self._resolve(raw_response).get("content")
        return isinstance(content, dict) and "application/json" in content

    # --- $ref resolution ----------------------------------------------------

    def _resolve(self, node: Dict[str, Any]) -> Dict[str, Any]:
        for _ in range(32):
            ref = node.get("$ref")
            if not isinstance(ref, str):
                return node
            nxt = self._resolve_ref(ref)
            if nxt is None:
                return {}
            node = nxt
        return node

    def _resolve_ref(self, ref: str) -> Optional[Dict[str, Any]]:
        if not ref.startswith("#/"):
            return None
        cur: Any = self.root
        for seg in ref[2:].split("/"):
            seg = seg.replace("~1", "/").replace("~0", "~")
            if not isinstance(cur, dict):
                return None
            cur = cur.get(seg)
        return cur if isinstance(cur, dict) else None

    # --- value synthesis ----------------------------------------------------

    def params_values(self, op: Operation) -> Dict[str, Any]:
        """Query and header parameters keyed by their spec names."""
        out: Dict[str, Any] = {}
        for param in op.params:
            name = param.get("name")
            if isinstance(name, str):
                out[name] = self.param_value(param)
        return out

    def param_value(self, param: Dict[str, Any]) -> Any:
        if "example" in param:
            return param["example"]
        schema = param.get("schema")
        return self._synth(schema if isinstance(schema, dict) else None)

    def body_variant_labels(self, op: Operation) -> Optional[List[str]]:
        """Labels of the request body's top-level oneOf/anyOf members, or None.

        Each member becomes its own case so that every variant is actually sent.
        """
        members = _variants(op.body_schema)
        if members is None:
            return None
        discriminator = (op.body_schema or {}).get("discriminator")
        discriminator = discriminator if isinstance(discriminator, dict) else {}
        return [_discriminator_value(discriminator, _ref_of(member)) for member in members]

    def body_value(self, op: Operation, variant_index: int) -> Any:
        members = _variants(op.body_schema)
        if members is not None and variant_index < len(members):
            return self._synth_variant(op.body_schema, members[variant_index])
        return self._synth(op.body_schema)

    def _synth(self, schema: Optional[Dict[str, Any]]) -> Any:
        if not isinstance(schema, dict):
            return None
        schema = self._resolve(schema)
        if "example" in schema:
            return schema["example"]
        enum = schema.get("enum")
        if isinstance(enum, list) and enum:
            return enum[0]
        members = _variants(schema)
        if members is not None:
            return self._synth_variant(schema, members[0])
        all_of = schema.get("allOf")
        if isinstance(all_of, list):
            return self._synth_object(self._merge_all_of(all_of))
        kind = schema.get("type")
        if kind is None and isinstance(schema.get("properties"), dict):
            kind = "object"
        if kind == "object":
            return self._synth_object(schema)
        if kind == "array":
            items = schema.get("items")
            item = self._synth(items if isinstance(items, dict) else None)
            return [item] if item is not None else []
        return _synth_scalar(schema)

    def _synth_object(self, schema: Dict[str, Any]) -> Dict[str, Any]:
        # Every declared property, not just the required ones: an optional
        # property that is never sent leaves its own serialization, and the
        # required fields nested below it, unverified.
        out: Dict[str, Any] = {}
        properties = schema.get("properties")
        if isinstance(properties, dict):
            for name, raw in properties.items():
                if isinstance(raw, dict):
                    out[name] = self._synth(raw)
        return out

    def _merge_all_of(self, members: List[Any]) -> Dict[str, Any]:
        props: Dict[str, Any] = {}
        for raw in members:
            if not isinstance(raw, dict):
                continue
            part = self._resolve(raw)
            part_props = part.get("properties")
            if isinstance(part_props, dict):
                props.update(part_props)
        return {"properties": props}

    def _synth_variant(self, parent: Optional[Dict[str, Any]], member: Any) -> Any:
        if not isinstance(member, dict):
            return {}
        value = self._synth(member)
        discriminator = (parent or {}).get("discriminator")
        if not isinstance(discriminator, dict) or not isinstance(value, dict):
            return value
        prop = discriminator.get("propertyName")
        if isinstance(prop, str):
            value[prop] = _discriminator_value(discriminator, _ref_of(member))
        return value


def _synth_scalar(schema: Dict[str, Any]) -> Any:
    kind = schema.get("type")
    if kind in ("integer", "number"):
        return 1
    if kind == "boolean":
        return True
    fmt = schema.get("format")
    if fmt == "date":
        return "2024-01-01"
    if fmt == "date-time":
        return "2024-01-01T00:00:00Z"
    # A string with no example still has to clear the declared length floor or
    # the mock rejects it. Padding with an alphanumeric also satisfies the
    # character patterns these specs declare.
    value = SYNTHETIC_VALUE
    min_len = _int_of(schema.get("minLength"))
    while len(value) < min_len:
        value += "x"
    return value


def _int_of(value: Any) -> int:
    if isinstance(value, (int, float)):
        return int(value)
    return 0


def _variants(schema: Optional[Dict[str, Any]]) -> Optional[List[Any]]:
    """The schema's oneOf or anyOf members, or None when it is neither."""
    if not isinstance(schema, dict):
        return None
    for keyword in ("oneOf", "anyOf"):
        members = schema.get(keyword)
        if isinstance(members, list) and members:
            return members
    return None


def _discriminator_value(discriminator: Dict[str, Any], ref: str) -> str:
    mapping = discriminator.get("mapping")
    if isinstance(mapping, dict):
        for value, target in mapping.items():
            if str(target) == ref and ref:
                return value
    if "/" in ref:
        return ref.rsplit("/", 1)[1]
    return SYNTHETIC_VALUE


def _ref_of(member: Any) -> str:
    if isinstance(member, dict):
        ref = member.get("$ref")
        if isinstance(ref, str):
            return ref
    return ""


def _stringify_keys(value: Any) -> Any:
    """Turn mapping keys into strings.

    Unquoted response codes (``200:``) decode to integer keys, so without this
    the document would carry two different key types.
    """
    if isinstance(value, dict):
        return {str(k): _stringify_keys(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_stringify_keys(v) for v in value]
    return value
