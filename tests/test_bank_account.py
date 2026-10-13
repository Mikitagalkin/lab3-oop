import pytest
from src.lab3.bank_account import BankAccount, InsufficientFundsError


def test_create():
    acc = BankAccount("Иван", 100)
    assert acc.balance == 100


def test_deposit():
    acc = BankAccount("Иван", 100)
    acc.deposit(50)
    assert acc.balance == 150


def test_withdraw():
    acc = BankAccount("Иван", 100)
    acc.withdraw(40)
    assert acc.balance == 60


def test_insufficient():
    acc = BankAccount("Иван", 100)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(200)


def test_negative_deposit():
    acc = BankAccount("Иван", 100)
    with pytest.raises(ValueError):
        acc.deposit(-10)