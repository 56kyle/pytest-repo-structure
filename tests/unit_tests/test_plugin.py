from pathlib import Path

import pytest
from _pytest.pytester import Pytester
from _pytest.pytester import RunResult


@pytest.mark.parametrize(
    argnames=["fixture_name", "expected_name"],
    argvalues=[
        ("repository_root", "test_fixture_path"),
        ("tests_folder", "tests"),
        ("unit_tests_folder", "unit_tests"),
        ("integration_tests_folder", "integration_tests"),
        ("acceptance_tests_folder", "acceptance_tests"),
        ("data_folder", "data"),
        ("configs_folder", "conf"),
    ],
)
def test_fixture_path(
    pytester: Pytester, conftest: str, fixture_name: str, expected_name: str
) -> None:
    fixture_test: Path = pytester.makepyfile(
        f"""
        import pytest

        from pathlib import Path


        def test_{fixture_name}({fixture_name}: Path) -> None:
            assert {fixture_name}.name.startswith({expected_name!r})
        """
    )
    result: RunResult = pytester.runpytest(fixture_test)
    result.assert_outcomes(passed=1)
