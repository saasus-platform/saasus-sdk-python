"""Entry point of the contract suite: ``pytest tests/contract``.

Each (operation, request-body variant) is its own parametrized case so that
failures are counted and named individually. A module with no Prism endpoint
contributes no case, so one module can be run locally and all of them in CI.

Local single-module run::

    CONTRACT_SPEC_DIR=... CONTRACT_MODULES=auth \\
        PRISM_URL_AUTH=http://127.0.0.1:4010 poetry run pytest tests/contract
"""

import pytest

import engine

# Without a spec directory there is nothing to mock against; the whole suite is
# skipped so a plain repo-wide ``pytest`` run does not require Prism.
_CONFIGURED = engine.spec_dir() is not None
pytestmark = pytest.mark.skipif(not _CONFIGURED, reason="CONTRACT_SPEC_DIR is not set")

_CASES = engine.build_cases() if _CONFIGURED else []


@pytest.mark.parametrize("case", _CASES, ids=[case.id for case in _CASES])
def test_contract(case):
    case.run()


def test_at_least_one_case_ran():
    # Guards a run that proved nothing: configured modules but no mock reachable,
    # or no spec operation resolving to a generated method.
    assert _CASES, "no operation case was built: no configured module has both a mock and a matching SDK method"


def test_module_list_is_provided():
    # CONTRACT_MODULES carries the module list from the fetch-openapi-spec
    # action; an empty value would silently test nothing.
    assert engine.configured_modules(), (
        "CONTRACT_MODULES is empty: it carries the module list from the fetch-openapi-spec action "
        "(locally: CONTRACT_MODULES=auth PRISM_URL_AUTH=http://127.0.0.1:4010 pytest tests/contract)"
    )


def test_every_generated_module_is_under_test():
    # A module generated into the SDK but absent from CONTRACT_MODULES yields no
    # case, leaving its operations unverified. Enforced only for the latest SDK
    # (B); a released SDK (C) or a local run legitimately covers fewer modules.
    if not engine.require_complete():
        pytest.skip("CONTRACT_REQUIRE_COMPLETE is not set: module coverage is only enforced for the latest SDK (B)")
    configured = set(engine.configured_modules())
    untested = [module for module in engine.generated_modules() if module not in configured]
    assert not untested, (
        "modules generated into the SDK but absent from CONTRACT_MODULES "
        f"(their operations would go unverified): {untested}"
    )


def test_all_operations_enumerated():
    # The latest SDK (B) must cover every spec operation; a released SDK (C)
    # legitimately lacks operations added later, so this is opt-in.
    if not engine.require_complete():
        pytest.skip("CONTRACT_REQUIRE_COMPLETE is not set: completeness is only enforced for the latest SDK (B)")
    missing = engine.unmapped_operations()
    assert not missing, f"spec operations not present in the SDK: {missing}"
