from pathlib import Path

import pytest
from _pytest.pytester import Pytester
from _pytest.pytester import RunResult

from pytest_repo_structure.plugin import __choose_default_fixture_path  # pyright: ignore[reportPrivateUsage]


def test___choose_default_fixture_path_with_no_hook_path(tmp_path: Path) -> None:
    assert __choose_default_fixture_path(hook_path=None, config_path=tmp_path) == tmp_path


def test___choose_default_fixture_path_with_hook_path(tmp_path: Path) -> None:
    path_a: Path = tmp_path / "a"
    path_b: Path = tmp_path / "b"
    assert __choose_default_fixture_path(hook_path=path_a, config_path=path_b) == path_a


def test___choose_default_fixture_path_with_invalid_hook_path(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="Received non Path value"):
        __choose_default_fixture_path(hook_path=2, config_path=tmp_path)


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
