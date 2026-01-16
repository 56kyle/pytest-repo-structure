import pytest

from pytest_repo_structure.hooks import pytest_acceptance_tests_folder
from pytest_repo_structure.hooks import pytest_config_folder
from pytest_repo_structure.hooks import pytest_data_folder
from pytest_repo_structure.hooks import pytest_integration_tests_folder
from pytest_repo_structure.hooks import pytest_plugin_tests_folder
from pytest_repo_structure.hooks import pytest_repository_root
from pytest_repo_structure.hooks import pytest_tests_folder
from pytest_repo_structure.hooks import pytest_unit_tests_folder


def test_pytest_repository_root_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_repository_root.__name__, None) is not None


def test_pytest_tests_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_tests_folder.__name__, None) is not None


def test_pytest_unit_tests_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_unit_tests_folder.__name__, None) is not None


def test_pytest_integration_tests_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_integration_tests_folder.__name__, None) is not None


def test_pytest_acceptance_tests_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_acceptance_tests_folder.__name__, None) is not None


def test_pytest_plugin_tests_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_plugin_tests_folder.__name__, None) is not None


def test_pytest_data_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_data_folder.__name__, None) is not None


def test_pytest_config_folder_registration(pytestconfig: pytest.Config) -> None:
    assert getattr(pytestconfig.hook, pytest_config_folder.__name__, None) is not None
