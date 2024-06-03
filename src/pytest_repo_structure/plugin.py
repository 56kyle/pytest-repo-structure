"""Main entrypoint for the pytest-repo-structure plugin."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope="session")
def repository_root(request: FixtureRequest) -> Path:
    """Path to the repository's root folder."""
    hook_path: Path | list[Any] = request.config.hook.pytest_repository_root()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", request.config.rootpath)


@pytest.fixture(scope="session")
def tests_folder(request: FixtureRequest, repository_root: Path) -> Path:
    """Path to the tests folder."""
    hook_path: Path | list[Any] = request.config.hook.pytest_tests_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", repository_root / "tests")


@pytest.fixture(scope="session")
def unit_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing unit tests."""
    hook_path: Path | list[Any] = request.config.hook.pytest_unit_tests_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", tests_folder / "unit_tests")


@pytest.fixture(scope="session")
def integration_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing integration tests."""
    hook_path: Path | list[Any] = request.config.hook.pytest_integration_tests_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", tests_folder / "integration_tests")


@pytest.fixture(scope="session")
def acceptance_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing acceptance tests."""
    hook_path: Path | list[Any] = request.config.hook.pytest_acceptance_tests_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", tests_folder / "acceptance_tests")


@pytest.fixture(scope="session")
def data_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test data."""
    hook_path: Path | list[Any] = request.config.hook.pytest_data_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", tests_folder / "data")


@pytest.fixture(scope="session")
def configs_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test configs."""
    hook_path: Path | list[Any] = request.config.hook.pytest_configs_folder()
    if hook_path:
        return getattr(request, "param", hook_path)
    return getattr(request, "param", tests_folder / "conf")
