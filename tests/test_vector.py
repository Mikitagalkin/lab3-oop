import pytest
from src.lab3.vector import Vector


def test_add():
    assert Vector(1, 2) + Vector(3, 4) == Vector(4, 6)


def test_add_different_sizes():
    with pytest.raises(ValueError):
        Vector(1, 2) + Vector(1, 2, 3)


def test_sub():
    assert Vector(5, 6) - Vector(1, 2) == Vector(4, 4)


def test_mul():
    assert Vector(1, 2) * 3 == Vector(3, 6)
    assert 3 * Vector(1, 2) == Vector(3, 6)


def test_len():
    assert len(Vector(1, 2, 3)) == 3