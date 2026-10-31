import pytest


def test_plugin_registration(pytestconfig: pytest.Config) -> None:
    assert pytestconfig.pluginmanager.hasplugin("pytest-repo-structure")
