from pathlib import Path

from _pytest.pytester import Pytester
from _pytest.pytester import RunResult


def test_plugin_registration(pytester: Pytester) -> None:
    path: Path = pytester.copy_example("test_plugin_registration")
    result: RunResult = pytester.runpytest(path, "-vv", "-s")
    result.assert_outcomes(passed=1)


def test_hook_registration(pytester: Pytester) -> None:
    path: Path = pytester.copy_example("test_hook_registration")
    result: RunResult = pytester.runpytest(path, "-vv", "-s")
    result.assert_outcomes(passed=8)


def test_fixture_registration(pytester: Pytester) -> None:
    path: Path = pytester.copy_example("test_fixture_registration")
    result: RunResult = pytester.runpytest(path, "-vv", "-s")
    result.assert_outcomes(passed=8)


def test_fixture_default_value_with_hook(pytester: Pytester) -> None:
    path: Path = pytester.copy_example("test_fixture_default_value_with_hook")
    result: RunResult = pytester.runpytest(path, "-vv", "-s")
    result.assert_outcomes(passed=8)


def test_fixture_default_value_with_no_hook(pytester: Pytester) -> None:
    path: Path = pytester.copy_example("test_fixture_default_value_with_no_hook")
    result: RunResult = pytester.runpytest(path, "-vv", "-s")
    result.assert_outcomes(passed=8)
