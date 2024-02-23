from bank_account.Account import Account


class Invalid_account_exception(BaseException):
    def __init__(self, message):
        super.__init__(message)


class Bank:
    def __init__(self, bank_name, accounts: list < Account > Account):
        self.bank_name = bank_name
        self.account_number = 1000
        self.accounts = list()

    def list(self, accounts):
        return self.accounts

    @staticmethod
    def get_account(self):
        return Account

    @staticmethod
    def generate_account_number(account_number):
        account_number += 1
        return account_number

    def register_customer(self, first_name: str, second_name: str, pin: str):
        account_number = self.generate_account_number(self.account_number)
        account = Account(first_name + '' + second_name, pin, account_number)
        self.accounts.add(account)
        return account

    def get_number_of_account(self):
        return self.accounts.size()

    def find_account(self, account_number: int):
        for account in self.accounts:
            if account.get_account() == account_number:
                return account
            raise Invalid_account_exception("account not found")

    def check_balance(self, pin: str, account_number: int):
        account = self.find_account(account_number)
        return account.self.get_balance(pin)

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
        self.accounts.remove(account_number)
