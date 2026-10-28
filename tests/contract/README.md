# SDK Contract Test (Python)

Round-trips the generated SDK clients against a [Prism](https://github.com/stoplightio/prism)
mock started from the latest OpenAPI spec, and checks three things on every pull
request (see `.github/workflows/sdk-contract-test.yml`):

- **(A) build / type-check** — the committed generated code byte-compiles and
  imports.
- **(B) spec compliance (latest SDK)** — every operation's request is accepted
  by the mock and its response deserializes into the SDK types, with no
  operation left unenumerated.
- **(C) forward compatibility (released SDK)** — the latest released tag's *own*
  bundled suite still round-trips against the *latest* spec.

The test is mock-only (Prism); it never touches the real API. Synthetic data
only: a constant bearer token and request values taken from the spec. Response
bodies, tokens, PII and the spec body are never logged.

## Layout

| File | Role |
|------|------|
| `spec.py` | Parses the OpenAPI document and synthesizes request inputs from `example`/schema. |
| `engine.py` | Resolves each spec `operationId` to a generated method, binds arguments by name, performs the round trip, and judges the result. |
| `test_contract.py` | Pytest entry point: one parametrized case per operation + watchdogs. |
| `test_synthesis.py` | Unit tests for input synthesis and argument binding (no mock). |

There is deliberately no `__init__.py`: pytest puts this directory on
`sys.path`, so the modules import each other by plain name, which keeps the
entry point identical across SDK generations for (C).

## Running locally

```bash
# one module
CONTRACT_SPEC_DIR=/path/to/spec-dir CONTRACT_MODULES=pricing \
  PRISM_URL_PRICING=http://127.0.0.1:4010 \
  poetry run pytest tests/contract

# unit tests only (no Prism, no env needed)
poetry run pytest tests/contract/test_synthesis.py
```

`CONTRACT_SPEC_DIR` holds the `<module>.yml` files; `CONTRACT_MODULES` is the
space-separated module list; `PRISM_URL_<MODULE>` gives each module's mock.
`CONTRACT_REQUIRE_COMPLETE=true` additionally fails (B) if a spec operation has
no matching SDK method. Without `CONTRACT_SPEC_DIR` the suite skips, so a plain
repo-wide `pytest` run does not require Prism.

## Python-specific notes

- **Call form.** Only `<operation>_with_http_info` is exercised. The plain
  `<operation>` form delegates to it and only unwraps `ApiResponse.data`, and
  `async_req=True` runs the same synchronous `call_api` on a worker thread;
  neither adds deserialization logic. `with_http_info` is also the only form
  that exposes the HTTP status together with the deserialized payload.
- **Operation enumeration.** A module's operations are spread across several
  `*Api` classes (grouped by tag), so the engine instantiates every `*Api`
  class under `saasus_sdk_python.src.<module>.api` and matches a spec
  `operationId` to a method by a normalized key (lower-cased, non-alphanumerics
  removed). An operation the SDK lacks simply has no case, which is what lets
  the same suite run against a previously released SDK.
- **Argument binding is by name.** Generated path/query/header arguments carry
  the spec parameter name in snake_case, so values bind by name rather than
  position and stay correct even when a spec revision inserts a parameter. An
  argument the spec cannot explain fails the case explicitly.
- **oneOf.** The generated models resolve oneOf via a `type` discriminator in
  `from_json` and raise on an unknown variant, so a normal deserialization
  already proves the union resolved; no separate union check is needed. On the
  request side the synthesized body is converted with the argument model's
  `from_dict`: a oneOf body is generated as a holder that only `from_dict`
  fills in, so the plain dict would never serialize.
- **Result.** Only a 2xx is a pass, and a method whose return type declares a
  body must deserialize into a non-null payload. An operation that declares no
  success response passes when it surfaces one of its declared error statuses.
