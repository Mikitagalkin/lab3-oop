"""Вектор с перегрузкой оператора +."""


class Vector:
    def __init__(self, *components: float):
        if not components:
            raise ValueError("Вектор не может быть пустым")
        self._components = tuple(float(c) for c in components)

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError("Разные размерности")
        return Vector(*(a + b for a, b in zip(self._components, other._components)))

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            raise ValueError("Разные размерности")
        return Vector(*(a - b for a, b in zip(self._components, other._components)))

    def __mul__(self, scalar: float):
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return Vector(*(c * scalar for c in self._components))

    __rmul__ = __mul__

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self._components == other._components

    def __len__(self) -> int:
        return len(self._components)

    def __getitem__(self, i: int) -> float:
        return self._components[i]

    def __repr__(self) -> str:
        return f"Vector({', '.join(map(str, self._components))})"