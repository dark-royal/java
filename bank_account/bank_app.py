import sys

from bank_account import bank
from bank_account.InvalidAmountException import InvalidAmountException
from bank_account.InvalidPinException import InvalidPinException
from bank_account.InvalidAccountException import InvalidAccountException
from bank_account.bank import Bank


class bank_app:
    bank = Bank("uba")

    def main_menu(self):
        print("""
              <><><>Welcome to your bank app<>
            <><><><><><><><><><><><><><><><><>
            Here are set of things you would like to do
                    1:create bank account
                    2:Deposit amount
                    3:Withdraw amount
                    4:Transfer amount
                    5:Remove account
                    6:Check balance
                    7:exit program    
            <><><><><><><><><<><><><><><><><><>       
        """)
        self.option()

    def option(self):
        option = input("Enter option to choose from")
        if option == '1':
            self.register_customer()

        elif option == '2':
            self.deposit()

        elif option == '3':
            self.withdraw()

        elif option == '4':
            self.transfer()

        elif option == '5':
            self.remove_account()

        elif option == '6':
            self.check_balance()

        elif option == '7':
            self.exit_program()

    def register_customer(self):
        first_name = input("Enter first name ")
        second_name = input("Enter second name")
        pin = input("Enter pin")
        account = self.bank.register_customer(first_name, second_name, pin)
        print("<><><><><><>Account created successfully<><><><><><><>")
        self.main_menu()

    def deposit(self):
        try:
            account_number = int(input("Enter account number"))
            amount = int(input("Enter amount"))
            account = self.bank.deposit(amount, account_number)
            print(f"<><><><>{amount} is deposited to {account_number} <><><><><><")
        except InvalidAccountException as error:
            print({error})

        except InvalidAmountException as error:
            print({error})

        finally:
            self.main_menu()

    def withdraw(self):
        try:
            account_number = int(input("Enter account number"))
            amount = int(input("Enter amount"))
            pin = input("Enter pin")
            account = self.bank.withdraw(account_number, amount, pin)
            print(f"<><><><>{amount} is withdrawn  from  {account_number} <><><><><><")
        except InvalidAccountException as error:
            print({error})

        except InvalidAmountException as error:
            print({error})

        except InvalidPinException as error:
            print({error})

        finally:
            self.main_menu()

    def transfer(self):
        try:
            amount = int(input("Enter amount"))
            receiver_account_number = int(input("Enter receiver account number"))
            sender_account_number = int(input("Enter sender account number"))
            pin = input("Enter pin")
            account = self.bank.transfer(amount, receiver_account_number, sender_account_number, pin)
            print(
                f"<><><><>{amount} is deposited to {sender_account_number} <><><><><>{amount} is transferred to {sender_account_number} ")
        except InvalidAmountException as error:
            print({error})

        except InvalidAccountException as error:
            print({error})

        except InvalidPinException as error:
            print({error})

        finally:
            self.main_menu()

    def remove_account(self):
        try:
            account_number = int(input("Enter pin"))
            pin = input("Enter pin")
            account = self.bank.remove_account(account_number, pin)
            print(f"<><><><>{account_number} is removed from list of account<><><><><><>")
        except InvalidAccountException as error:
            print({error})
        except InvalidPinException as error:
            print({error})

        finally:
            self.main_menu()

    def check_balance(self):
        try:
            account_number = int(input("Enter account number"))
            pin = input("Enter pin")
            account = self.bank.check_balance(pin, account_number)
            print(f"<><><><>{account_number} balance is  {account} <><><><><><")
        except InvalidAccountException as error:
            print({error})
        except InvalidPinException as error:
            print({error})
        finally:
            self.main_menu()

    @staticmethod
    def exit_program():
        sys.exit(0)


bank1 = bank_app()
bank1.main_menu()
