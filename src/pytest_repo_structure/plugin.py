"""Main entrypoint for the pytest-repo-structure plugin."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any

import pytest

from pytest_repo_structure.constants import DEFAULT_ACCEPTANCE_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_CONFIG_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_DATA_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_INTEGRATION_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_PLUGIN_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_UNIT_TESTS_FOLDER_NAME


if TYPE_CHECKING:
    from _pytest.config import PytestPluginManager
    from _pytest.fixtures import FixtureRequest


def pytest_addhooks(pluginmanager: PytestPluginManager) -> None:
    """Pytest hook used for adding new hooks."""
    from pytest_repo_structure import hooks

    pluginmanager.add_hookspecs(hooks)


def __choose_default_fixture_path(hook_path: Any, config_path: Path) -> Path:
    """Returns and validates the default path to be used if a fixture fails to provide an override."""
    if hook_path is None:
        return config_path
    if not isinstance(hook_path, Path):
        raise ValueError(f"Received non Path value of '{hook_path}'.")
    return hook_path


@pytest.fixture(scope="session")
def repository_root(request: FixtureRequest) -> Path:
    """Path to the repository's root folder."""
    hook_path: Any = request.config.hook.pytest_repository_root()
    config_path: Path = request.config.rootpath
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def tests_folder(request: FixtureRequest, repository_root: Path) -> Path:
    """Path to the tests folder."""
    hook_path: Any = request.config.hook.pytest_tests_folder()
    config_path: Path = repository_root / DEFAULT_TESTS_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def unit_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing unit tests."""
    hook_path: Any = request.config.hook.pytest_unit_tests_folder()
    config_path: Path = tests_folder / DEFAULT_UNIT_TESTS_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def integration_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing integration tests."""
    hook_path: Any = request.config.hook.pytest_integration_tests_folder()
    config_path: Path = tests_folder / DEFAULT_INTEGRATION_TESTS_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def acceptance_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing acceptance tests."""
    hook_path: Any = request.config.hook.pytest_acceptance_tests_folder()
    config_path: Path = tests_folder / DEFAULT_ACCEPTANCE_TESTS_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def plugin_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing acceptance tests."""
    hook_path: Any = request.config.hook.pytest_plugin_tests_folder()
    config_path: Path = tests_folder / DEFAULT_PLUGIN_TESTS_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def data_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test data."""
    hook_path: Any = request.config.hook.pytest_data_folder()
    config_path: Path = tests_folder / DEFAULT_DATA_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)


@pytest.fixture(scope="session")
def config_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test configs."""
    hook_path: Any = request.config.hook.pytest_config_folder()
    config_path: Path = tests_folder / DEFAULT_CONFIG_FOLDER_NAME
    default_path: Path = __choose_default_fixture_path(hook_path=hook_path, config_path=config_path)
    return getattr(request, "param", default_path)
