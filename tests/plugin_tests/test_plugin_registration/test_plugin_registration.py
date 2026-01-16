import pytest


def test_plugin_registration(pytestconfig: pytest.Config) -> None:
    assert pytestconfig.pluginmanager.hasplugin("pytest_repo_structure.plugin")
