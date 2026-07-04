from typing import Any

import pytest

from pytest_repo_structure.plugin import acceptance_tests_folder
from pytest_repo_structure.plugin import config_folder
from pytest_repo_structure.plugin import data_folder
from pytest_repo_structure.plugin import integration_tests_folder
from pytest_repo_structure.plugin import plugin_tests_folder
from pytest_repo_structure.plugin import repository_root
from pytest_repo_structure.plugin import tests_folder
from pytest_repo_structure.plugin import unit_tests_folder


@pytest.mark.parametrize(
    argnames="fixture",
    argvalues=[
        repository_root,
        tests_folder,
        acceptance_tests_folder,
        config_folder,
        data_folder,
        integration_tests_folder,
        plugin_tests_folder,
        unit_tests_folder,
    ],
)
def test_plugin_module_fixtures(fixture: Any) -> None:
    assert fixture is not None
