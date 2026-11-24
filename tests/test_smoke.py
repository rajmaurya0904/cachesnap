"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import cachesnap


def test_version_is_set() -> None:
    assert cachesnap.__version__
