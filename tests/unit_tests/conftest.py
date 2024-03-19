"""Fixtures used in unit tests."""

from __future__ import annotations

from pathlib import Path

import pytest
from _pytest.fixtures import FixtureRequest
from _pytest.pytester import Pytester


@pytest.fixture(scope="function")
def conftest(request: FixtureRequest, pytester: Pytester, conftest_source: str) -> Path:
    conftest_path: Path = pytester.makeconftest(source=conftest_source)
    return getattr(request, "param", conftest_path)


@pytest.fixture(scope="function")
def conftest_source(request: FixtureRequest, conftest_source_path: Path) -> str:
    conftest_source: str | None = getattr(request, "param", None)
    if conftest_source is not None:
        return conftest_source
    return conftest_source_path.read_text()


@pytest.fixture(scope="function")
def conftest_source_path(request: FixtureRequest, data_folder: Path) -> Path:
    return getattr(request, "param", data_folder / "example_conftest.py")
