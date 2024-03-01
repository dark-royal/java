from bank_account.Account import Account

from bank_account.InvalidAccountException import InvalidAccountException
from bank_account.InvalidPinException import InvalidPinException


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.account_number = 1
        self.accounts = []

    def register_customer(self, first_name: str, second_name: str, pin: str):
        account = Account(first_name + '' + second_name, pin, self.account_number)
        self.account_number += 1
        self.accounts.append(account)
        return account

    def get_number_of_account(self):
        return len(self.accounts)

    def find_account(self, account_number: int) -> Account:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        raise InvalidAccountException("Account not found")

    def get_account(self):
        return self.account_number

    def check_balance(self, pin: str, account_number: int):
        account = self.find_account(account_number)
        return account.get_balance(pin)

    def deposit(self, amount: int, account_number):
        account = self.find_account(account_number)
        account.deposit(amount)

    def withdraw(self, account_number: int, amount: int, pin: str):
        account = self.find_account(account_number)
        account.withdraw(amount, pin)

    def transfer(self, amount: int, receiver_account_number: int, sender_account_number: int, pin: str):
        sender_account_num = self.find_account(sender_account_number)
        receiver_account_num = self.find_account(receiver_account_number)
        sender_account_num.withdraw(amount, pin)
        receiver_account_num.deposit(amount)

    def remove_account(self, account_number: int, pin: str):
        account = self.find_account(account_number)
        account.validate_pin(pin)
        self.accounts.remove(account)
