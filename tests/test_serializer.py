import json
from src.lab3.serializer import Person, Address


def test_to_json():
    p = Person("Иван", 30)
    data = json.loads(p.to_json())
    assert data["name"] == "Иван"
    assert data["age"] == 30


def test_nested():
    addr = Address("ул. Ленина, 1", "Москва", "Россия", "101000")
    p = Person("Иван", 30, address=addr)
    data = p.to_dict()
    assert data["address"]["city"] == "Москва"


def test_from_json():
    p = Person("Иван", 30, "i@mail.ru")
    restored = Person.from_json(p.to_json())
    assert restored.name == "Иван"