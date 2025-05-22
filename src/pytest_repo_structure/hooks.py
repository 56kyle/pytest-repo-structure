"""Pytest hook specifications."""

from pathlib import Path

from _pytest.config import hookspec


@hookspec(firstresult=True)
def pytest_repository_root() -> Path:
    """Path to the repository's root folder."""


@hookspec(firstresult=True)
def pytest_tests_folder() -> Path:
    """Path to the tests folder."""


@hookspec(firstresult=True)
def pytest_unit_tests_folder() -> Path:
    """Returns the folder containing unit tests."""


@hookspec(firstresult=True)
def pytest_integration_tests_folder() -> Path:
    """Returns the folder containing integration tests."""


@hookspec(firstresult=True)
def pytest_acceptance_tests_folder() -> Path:
    """Returns the folder containing acceptance tests."""


@hookspec(firstresult=True)
def pytest_plugin_tests_folder() -> Path:
    """Returns the folder containing plugin tests."""


@hookspec(firstresult=True)
def pytest_data_folder() -> Path:
    """Returns the folder containing test data."""


@hookspec(firstresult=True)
def pytest_config_folder() -> Path:
    """Returns the folder containing test configs."""
