"""Мини-ORM: класс Таблица."""

from typing import Any, Optional


class Table:
    def __init__(self, name: str, columns: list):
        if not name or not columns:
            raise ValueError("Имя и колонки обязательны")
        self.name = name
        self.columns = list(columns)
        self._rows = []
        self._next_id = 1

    def insert(self, **kwargs: Any) -> dict:
        for k in kwargs:
            if k not in self.columns:
                raise ValueError(f"Неизвестная колонка: {k}")
        row = {"_id": self._next_id}
        self._next_id += 1
        for col in self.columns:
            row[col] = kwargs.get(col)
        self._rows.append(row)
        return row.copy()

    def select(self, where: Optional[dict] = None) -> list:
        return [r.copy() for r in self._rows if self._match(r, where)]

    def update(self, where: dict, **kwargs: Any) -> int:
        for k in kwargs:
            if k not in self.columns:
                raise ValueError(f"Неизвестная колонка: {k}")
        count = 0
        for r in self._rows:
            if self._match(r, where):
                for k, v in kwargs.items():
                    r[k] = v
                count += 1
        return count

    def delete(self, where: dict) -> int:
        before = len(self._rows)
        self._rows = [r for r in self._rows if not self._match(r, where)]
        return before - len(self._rows)

    def count(self) -> int:
        return len(self._rows)

    @staticmethod
    def _match(row: dict, where: Optional[dict]) -> bool:
        if not where:
            return True
        return all(row.get(k) == v for k, v in where.items())