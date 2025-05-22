from pathlib import Path

from tests.constants import CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_repository_root_default_value_with_hook(repository_root: Path) -> None:
    assert repository_root is not None
    assert repository_root == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_tests_folder_default_value_with_hook(tests_folder: Path) -> None:
    assert tests_folder is not None
    assert tests_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_unit_tests_folder_default_value_with_hook(unit_tests_folder: Path) -> None:
    assert unit_tests_folder is not None
    assert unit_tests_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_integration_tests_folder_default_value_with_hook(integration_tests_folder: Path) -> None:
    assert integration_tests_folder is not None
    assert integration_tests_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_acceptance_tests_folder_default_value_with_hook(acceptance_tests_folder: Path) -> None:
    assert acceptance_tests_folder is not None
    assert acceptance_tests_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_plugin_tests_folder_default_value_with_hook(plugin_tests_folder: Path) -> None:
    assert plugin_tests_folder is not None
    assert plugin_tests_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_data_folder_default_value_with_hook(data_folder: Path) -> None:
    assert data_folder is not None
    assert data_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE


def test_config_folder_default_value_with_hook(config_folder: Path) -> None:
    assert config_folder is not None
    assert config_folder == CUSTOM_HOOK_TEST_DEFAULT_VALUE
