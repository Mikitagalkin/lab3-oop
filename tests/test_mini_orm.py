import pytest
from src.lab3.mini_orm import Table


@pytest.fixture
def users():
    return Table("users", ["name", "age"])


def test_insert(users):
    users.insert(name="Alice", age=30)
    assert users.count() == 1


def test_select_all(users):
    users.insert(name="Alice", age=30)
    users.insert(name="Bob", age=25)
    assert len(users.select()) == 2


def test_select_where(users):
    users.insert(name="Alice", age=30)
    users.insert(name="Bob", age=25)
    rows = users.select(where={"name": "Alice"})
    assert len(rows) == 1


def test_update(users):
    users.insert(name="Alice", age=30)
    users.update(where={"name": "Alice"}, age=31)
    assert users.select(where={"name": "Alice"})[0]["age"] == 31


def test_delete(users):
    users.insert(name="Alice", age=30)
    users.insert(name="Bob", age=25)
    assert users.delete(where={"name": "Alice"}) == 1
    assert users.count() == 1


def test_invalid_column(users):
    with pytest.raises(ValueError):
        users.insert(unknown="x")