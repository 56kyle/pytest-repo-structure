from pathlib import Path

from tests.constants import CUSTOM_HOOK_TEST_DEFAULT_VALUE


pytest_plugins: list[str] = ["pytest-repo-structure"]


def pytest_repository_root() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_tests_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_unit_tests_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_integration_tests_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_acceptance_tests_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_plugin_tests_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_data_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE


def pytest_config_folder() -> Path:
    return CUSTOM_HOOK_TEST_DEFAULT_VALUE
