from decimal import Decimal

from bank_account.Exception import InvalidAmountException,InsufficientFundsException,InvalidPinException,AccountNotFoundException



class Account:
    balance = 0

    def __init__(self, name: str, pin: str, number: int):
        self.balance = 0
        self.name = name
        self.pin = pin
        self.number = number

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountException("Amount must be positive")
        self.balance += amount

    def set_pin(self, pin):
        self.pin = pin

    def get_pin(self):
        return self.pin

    def get_balance(self):
        return self.balance

    def set_account_number(self, balance):
        self.number = balance

    def get_account_number(self):
        return self.number

    def withdraw(self, amount,pin):
        if amount < 0 & amount > self.balance:
            if(self.pin)
            raise InsufficientFundsException("Insufficient funds")
        self.balance -= amount

