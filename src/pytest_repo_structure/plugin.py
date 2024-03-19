"""Main entrypoint for the pytest-repo-structure plugin."""

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest


@pytest.fixture(scope="session")
def repository_root(request: FixtureRequest) -> Path:
    """Path to the repository's root folder."""
    return getattr(request, "param", request.config.rootpath)


@pytest.fixture(scope="session")
def tests_folder(request: FixtureRequest, repository_root: Path) -> Path:
    """Path to the tests folder."""
    return getattr(request, "param", repository_root / "tests")


@pytest.fixture(scope="session")
def unit_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing unit tests."""
    return getattr(request, "param", tests_folder / "unit_tests")


@pytest.fixture(scope="session")
def integration_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing integration tests."""
    return getattr(request, "param", tests_folder / "integration_tests")


@pytest.fixture(scope="session")
def acceptance_tests_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing acceptance tests."""
    return getattr(request, "param", tests_folder / "acceptance_tests")


@pytest.fixture(scope="session")
def data_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test data."""
    return getattr(request, "param", tests_folder / "data")


@pytest.fixture(scope="session")
def configs_folder(request: FixtureRequest, tests_folder: Path) -> Path:
    """Returns the folder containing test configs."""
    return getattr(request, "param", tests_folder / "conf")
