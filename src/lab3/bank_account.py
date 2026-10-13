"""Банковский счёт."""


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.owner = owner
        self._balance = initial_balance
        self._history = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        self._balance += amount
        self._history.append(("deposit", amount))
        return self._balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        if amount > self._balance:
            raise InsufficientFundsError("Недостаточно средств")
        self._balance -= amount
        self._history.append(("withdraw", amount))
        return self._balance

    def get_history(self) -> list:
        return self._history.copy()

    def __repr__(self) -> str:
        return f"BankAccount({self.owner!r}, {self._balance})"