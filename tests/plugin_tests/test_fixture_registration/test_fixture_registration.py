"""Module responsible for testing fixture registration."""

from pathlib import Path


def test_repository_root_registration(repository_root: Path) -> None:
    assert repository_root is not None


def test_tests_folder_registration(tests_folder: Path) -> None:
    assert tests_folder is not None


def test_unit_tests_folder_registration(unit_tests_folder: Path) -> None:
    assert unit_tests_folder is not None


def test_integration_tests_folder_registration(integration_tests_folder: Path) -> None:
    assert integration_tests_folder is not None


def test_acceptance_tests_folder_registration(acceptance_tests_folder: Path) -> None:
    assert acceptance_tests_folder is not None


def test_plugin_tests_folder_registration(plugin_tests_folder: Path) -> None:
    assert plugin_tests_folder is not None


def test_data_folder_registration(data_folder: Path) -> None:
    assert data_folder is not None


def test_config_folder_registration(config_folder: Path) -> None:
    assert config_folder is not None
