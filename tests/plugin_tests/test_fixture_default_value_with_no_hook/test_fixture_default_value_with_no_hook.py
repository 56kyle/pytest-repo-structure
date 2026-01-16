from pathlib import Path

from _pytest.fixtures import FixtureRequest

from pytest_repo_structure.constants import DEFAULT_ACCEPTANCE_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_CONFIG_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_DATA_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_INTEGRATION_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_PLUGIN_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_TESTS_FOLDER_NAME
from pytest_repo_structure.constants import DEFAULT_UNIT_TESTS_FOLDER_NAME


def test_repository_root_default_value_with_no_hook(request: FixtureRequest, repository_root: Path) -> None:
    assert repository_root is not None
    assert repository_root.name == request.config.rootpath.name


def test_tests_folder_default_value_with_no_hook(tests_folder: Path) -> None:
    assert tests_folder is not None
    assert tests_folder.name == DEFAULT_TESTS_FOLDER_NAME


def test_unit_tests_folder_default_value_with_no_hook(unit_tests_folder: Path) -> None:
    assert unit_tests_folder is not None
    assert unit_tests_folder.name == DEFAULT_UNIT_TESTS_FOLDER_NAME


def test_integration_tests_folder_default_value_with_no_hook(integration_tests_folder: Path) -> None:
    assert integration_tests_folder is not None
    assert integration_tests_folder.name == DEFAULT_INTEGRATION_TESTS_FOLDER_NAME


def test_acceptance_tests_folder_default_value_with_no_hook(acceptance_tests_folder: Path) -> None:
    assert acceptance_tests_folder is not None
    assert acceptance_tests_folder.name == DEFAULT_ACCEPTANCE_TESTS_FOLDER_NAME


def test_plugin_tests_folder_default_value_with_no_hook(plugin_tests_folder: Path) -> None:
    assert plugin_tests_folder is not None
    assert plugin_tests_folder.name == DEFAULT_PLUGIN_TESTS_FOLDER_NAME


def test_data_folder_default_value_with_no_hook(data_folder: Path) -> None:
    assert data_folder is not None
    assert data_folder.name == DEFAULT_DATA_FOLDER_NAME


def test_config_folder_default_value_with_no_hook(config_folder: Path) -> None:
    assert config_folder is not None
    assert config_folder.name == DEFAULT_CONFIG_FOLDER_NAME
