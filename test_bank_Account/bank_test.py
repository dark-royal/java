import unittest

from bank_account.InsufficientFundsException import InsufficientFundsException
from bank_account.InvalidAmountException import InvalidAmountException
from bank_account.InvalidPinException import InvalidPinException
# from bank_account.InvalidAmountException import InvalidAmountException
from bank_account.bank import Bank


class MyTestCase(unittest.TestCase):

    def test_account_can_register_account(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "1234")
        self.assertEqual(1, bank.get_number_of_account())

    def test_account_can_register_two_account(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "1234")
        account1 = bank.register_customer("senior1", "dev2", "11110")
        self.assertEqual(2, bank.get_number_of_account())

    def test_account_can_deposit_3k(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        bank.deposit(3000, 1)
        self.assertEqual(3000, bank.check_balance("pin", 1))

    def test_can_deposit_3k_and_2k(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "1234")
        bank.deposit(3000, 1)
        bank.deposit(2000, 1)
        self.assertEqual(5000, bank.check_balance("1234", 1))

    def test_can_deposit_5k_2k_can_be_withdrawn(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        bank.withdraw(2, 2000, "pin1")
        self.assertEqual(3000, bank.check_balance("pin1", 2))

    def test_bank_can_deposit_5k_withdraw_6k_raise_invalid_amount_exception(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        with self.assertRaises(InsufficientFundsException):
            bank.withdraw(2, 6000, "pin1")
        self.assertEqual(5000, bank.check_balance("pin1", 2))

    def test_bank_can_deposit_5k_withdraw_negative_amount_raise_invalid_amount_exception(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        with self.assertRaises(InsufficientFundsException):
            bank.withdraw(2, -2000, "pin1")
        self.assertEqual(5000, bank.check_balance("pin1", 2))

    def test_that_can_deposit_5k_withdraw_2k_with_incorrect_password_raise_invalid_pin_exceptiom(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            bank.withdraw(2, 2000, "pini")
        self.assertEqual(5000, bank.check_balance("pin1", 2))

    def test_that_bank_can_transfer(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        bank.transfer(3000, 1, 2, "pin1")

        self.assertEqual(2000, bank.check_balance("pin1", 2))

    def test_that_account_can_transfer_with_incorrectPassword_raise_invalid_pin_exception(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            bank.transfer(2000, 1, 2, "pint")

    def test_that_bank_can_find_account(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.find_account(1)
        self.assertEqual(account, bank.find_account(1))

    def test_that_bank_can_find_account_and_can_remove_account(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.remove_account(1, "pin")
        self.assertEqual(1, bank.get_number_of_account())

    def test_bank_can_check_balance(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        self.assertEqual(5000, bank.check_balance("pin1", 2))

    def test_bank_can_check_balance_with_incorrect_pin_raise_invalid_pin_exception(self):
        bank = Bank("uba")
        account = bank.register_customer("senior", "dev", "pin")
        account1 = bank.register_customer("senior1", "dev1", "pin1")
        bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            bank.check_balance("pin2", 2)
