"""Сериализация в JSON."""

import json
import datetime
from typing import Any


class Serializable:
    def to_dict(self) -> dict:
        result = {}
        for key, value in self.__dict__.items():
            if key.startswith("_"):
                continue
            result[key] = self._serialize(value)
        return result

    @staticmethod
    def _serialize(value: Any) -> Any:
        if isinstance(value, Serializable):
            return value.to_dict()
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.isoformat()
        if isinstance(value, list):
            return [Serializable._serialize(v) for v in value]
        return value

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=indent)

    @classmethod
    def from_dict(cls, data: dict) -> "Serializable":
        obj = cls.__new__(cls)
        for k, v in data.items():
            setattr(obj, k, v)
        return obj

    @classmethod
    def from_json(cls, s: str) -> "Serializable":
        return cls.from_dict(json.loads(s))


class Address(Serializable):
    def __init__(self, street: str, city: str, country: str, zip_code: str):
        self.street = street
        self.city = city
        self.country = country
        self.zip_code = zip_code


class Person(Serializable):
    def __init__(self, name: str, age: int, email: str = None, address: Address = None):
        self.name = name
        self.age = age
        self.email = email
        self.address = address