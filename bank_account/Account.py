# from bank_account import InsufficientFundsException, InvalidPinException
from bank_account.InsufficientFundsException import InsufficientFundsException
from bank_account.InvalidAmountException import InvalidAmountException
from bank_account.InvalidPinException import InvalidPinException
from bank_account.invalid_name_exception import InvalidNameException


class Account:

    def __init__(self, name: str, pin: str, number: int):
        self.name = name
        self.pin = pin
        self.number = number
        self.balance = 0

    def get_balance(self, pin):
        self.validate_pin(pin)
        return self.balance

    def get_account_number(self):
        return self.number

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountException("Invalid Amount...")
        self.balance += amount

    def withdraw(self, amount, pin):
        self.validate_amount(amount)
        self.validate_pin(pin)
        self.balance -= amount
        pass

    def validate_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinException("Invalid pin....")
        return pin

    def validate_name(self):
        if not self.name:
            raise InvalidNameException("Name is not added")
        return self.name

    def validate_amount(self, amount):
        if amount < 0 or amount > self.balance:
            raise InsufficientFundsException("insufficient funds...")

