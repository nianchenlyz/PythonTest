"""
Asserting that a certain exception is raised
"""
import pytest


def raise_exception():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        raise_exception()
