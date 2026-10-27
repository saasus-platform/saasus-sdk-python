"""Input synthesis and argument binding on their own, without a mock.

The production specs declare neither header parameters nor anyOf request
bodies, so the round-trip suite would not exercise either path; the
forward-compatibility binding shapes only occur against a released SDK. These
tests cover them directly. They run unconditionally (no Prism, no env).
"""

import textwrap
from typing import Optional

import pytest

import engine
from engine import ContractFailure, build_kwargs
from spec import Spec

_PARAM_SPEC = """
    openapi: 3.0.0
    paths:
      /tenants/{tenant_id}/users:
        parameters:
          - name: tenant_id
            in: path
            schema:
              type: string
            example: tenant-1
        get:
          operationId: GetUsers
          parameters:
            - name: limit
              in: query
              schema:
                type: integer
              example: 10
            - name: X-Saasus-Referer
              in: header
              schema:
                type: string
              example: referer-1
          responses:
            200:
              description: ok
      /ping:
        get:
          operationId: Ping
          parameters:
            - name: X-Request-Id
              in: header
              schema:
                type: string
              example: req-1
          responses:
            200:
              description: ok
"""

_RESERVED_WORD_SPEC = """
    openapi: 3.0.0
    paths:
      /tenants/{tenant_id}/counts/{date}:
        get:
          operationId: GetDateCount
          parameters:
            - name: tenant_id
              in: path
              schema:
                type: string
              example: tenant-1
            - name: date
              in: path
              schema:
                type: string
              example: "2024-01-01"
          responses:
            200:
              description: ok
"""

_BODY_SPEC = """
    openapi: 3.0.0
    paths:
      /units:
        post:
          operationId: SaveUnit
          requestBody:
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnitForSave'
          responses:
            200:
              description: ok
    components:
      schemas:
        UnitForSave:
          KEYWORD:
            - $ref: '#/components/schemas/FixedUnit'
            - $ref: '#/components/schemas/UsageUnit'
          discriminator:
            propertyName: type
            mapping:
              fixed: '#/components/schemas/FixedUnit'
              usage: '#/components/schemas/UsageUnit'
        FixedUnit:
          type: object
          properties:
            name:
              type: string
              example: fixed-unit
        UsageUnit:
          type: object
          properties:
            name:
              type: string
              example: usage-unit
"""


def _write_spec(tmp_path, document):
    (tmp_path / "test.yml").write_text(textwrap.dedent(document))
    return Spec.load(str(tmp_path), "test")


def test_params_values_include_headers(tmp_path):
    # The generated method takes each query and header parameter as its own
    # argument; dropping the headers would leave an operation whose only
    # parameters are headers with no argument at all.
    spec = _write_spec(tmp_path, _PARAM_SPEC)
    assert spec.params_values(spec.ops["GetUsers"]) == {"limit": 10, "X-Saasus-Referer": "referer-1"}
    assert spec.params_values(spec.ops["Ping"]) == {"X-Request-Id": "req-1"}
    # The path parameter stays a positional/path argument, not a query/header one.
    assert len(spec.ops["GetUsers"].path_params) == 1


@pytest.mark.parametrize("keyword", ["oneOf", "anyOf"])
def test_body_variants_cover_oneof_and_anyof(tmp_path, keyword):
    # Every member of a composite request body is sent, for anyOf as well as
    # oneOf; otherwise a member reachable only through anyOf would be
    # synthesized as an empty object.
    spec = _write_spec(tmp_path, _BODY_SPEC.replace("KEYWORD", keyword))
    op = spec.ops["SaveUnit"]
    assert spec.body_variant_labels(op) == ["fixed", "usage"]
    assert spec.body_value(op, 1) == {"name": "usage-unit", "type": "usage"}


# Stand-ins for the generated signatures. Only their parameter names matter;
# they are never invoked.
def _current_signature(tenant_id, limit=None, x_saasus_referer=None):
    pass


def _older_signature(tenant_id, x_saasus_referer=None):
    pass


def _unexplained_signature(tenant_id, limit=None, x_saasus_referer=None, surprise=None):
    pass


# openapi-generator renames ``date`` (a reserved word) to ``var_date``.
def _reserved_word_signature(tenant_id, var_date):
    pass


def test_binds_path_query_and_header_parameters_by_name(tmp_path):
    spec = _write_spec(tmp_path, _PARAM_SPEC)
    op = spec.ops["GetUsers"]
    assert build_kwargs(_current_signature, spec, op, 0) == {
        "tenant_id": "tenant-1",
        "limit": 10,
        "x_saasus_referer": "referer-1",
    }


def test_binds_reserved_word_parameter_renamed_by_generator(tmp_path):
    # openapi-generator renames a spec parameter colliding with a Python
    # builtin/keyword (``date`` -> ``var_date``); the value must still bind to
    # that argument rather than being reported as unexplained.
    spec = _write_spec(tmp_path, _RESERVED_WORD_SPEC)
    op = spec.ops["GetDateCount"]
    assert build_kwargs(_reserved_word_signature, spec, op, 0) == {
        "tenant_id": "tenant-1",
        "var_date": "2024-01-01",
    }


def test_tolerates_parameter_missing_from_older_sdk(tmp_path):
    # An SDK generated before the spec added ``limit`` has no such argument;
    # that backward-compatible change must not fail. The value is simply dropped.
    spec = _write_spec(tmp_path, _PARAM_SPEC)
    op = spec.ops["GetUsers"]
    assert build_kwargs(_older_signature, spec, op, 0) == {
        "tenant_id": "tenant-1",
        "x_saasus_referer": "referer-1",
    }


def test_fails_on_argument_the_spec_does_not_explain(tmp_path):
    # Binding by position would send a plausible-looking request with the wrong
    # value, so an unexplained argument fails explicitly instead.
    spec = _write_spec(tmp_path, _PARAM_SPEC)
    op = spec.ops["GetUsers"]
    with pytest.raises(ContractFailure):
        build_kwargs(_unexplained_signature, spec, op, 0)


class _BodyModel:
    """Stand-in for a generated request-body model: only ``from_dict`` builds it."""

    def __init__(self, obj):
        self.obj = obj

    @classmethod
    def from_dict(cls, obj: dict) -> "_BodyModel":
        return cls(obj)


def _body_signature(body: Optional[_BodyModel] = None):
    pass


def test_body_is_converted_into_the_generated_model(tmp_path):
    # The generated models are not plain containers: a oneOf body is a holder
    # that only from_dict fills in, so passing the synthesized dict straight
    # through would serialize an empty body -- or fail before the request is
    # sent. The conversion must also see through the Optional[...] annotation.
    spec = _write_spec(tmp_path, _BODY_SPEC.replace("KEYWORD", "oneOf"))
    op = spec.ops["SaveUnit"]
    body = build_kwargs(_body_signature, spec, op, 1)["body"]
    assert isinstance(body, _BodyModel)
    assert body.obj == {"name": "usage-unit", "type": "usage"}


def test_module_absent_from_the_sdk_keeps_its_operations_in_the_completeness_check(tmp_path, monkeypatch):
    # A module the spec list carries but the SDK does not must not drop out of
    # the completeness check: otherwise all of its operations would go
    # unverified while the suite still passed.
    _write_spec(tmp_path, _PARAM_SPEC)
    monkeypatch.setenv("CONTRACT_SPEC_DIR", str(tmp_path))
    monkeypatch.setenv("CONTRACT_MODULES", "test")
    monkeypatch.setenv("PRISM_URL_TEST", "http://127.0.0.1:4010")
    monkeypatch.setattr(engine, "_modules_cache", None)

    assert engine.build_cases() == []
    assert engine.unmapped_operations() == ["test.GetUsers", "test.Ping"]
