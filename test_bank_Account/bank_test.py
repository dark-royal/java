import unittest

from bank_account.InsufficientFundsException import InsufficientFundsException
from bank_account.InvalidPinException import InvalidPinException
from bank_account.bank import Bank


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("uba")

    def test_account_can_register_account(self):
        account = self.bank.register_customer("senior", "dev", "1234")
        self.assertEqual(1,self.bank.get_number_of_account())

    def test_account_can_register_two_account(self):
        account = self.bank.register_customer("senior", "dev", "1234")
        account1 = self.bank.register_customer("senior1", "dev2", "11110")
        self.assertEqual(2, self.bank.get_number_of_account())

    def test_account_can_deposit_3k(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        self.bank.deposit(3000, 1)
        self.assertEqual(3000, self.bank.check_balance("pin", 1))

    def test_can_deposit_3k_and_2k(self):
        account = self.bank.register_customer("senior", "dev", "1234")
        self.bank.deposit(3000, 1)
        self.bank.deposit(2000, 1)
        self.assertEqual(5000, self.bank.check_balance("1234", 1))

    def test_can_deposit_5k_2k_can_be_withdrawn(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        self.bank.withdraw(2, 2000, "pin1")
        self.assertEqual(3000, self.bank.check_balance("pin1", 2))

    def test_bank_can_deposit_5k_withdraw_6k_raise_invalid_amount_exception(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(2, 6000, "pin1")
        self.assertEqual(5000, self.bank.check_balance("pin1", 2))

    def test_bank_can_deposit_5k_withdraw_negative_amount_raise_invalid_amount_exception(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(2, -2000, "pin1")
        self.assertEqual(5000, self.bank.check_balance("pin1", 2))

    def test_that_can_deposit_5k_withdraw_2k_with_incorrect_password_raise_invalid_pin_exceptiom(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            self.bank.withdraw(2, 2000, "pini")
        self.assertEqual(5000, self.bank.check_balance("pin1", 2))

    def test_that_bank_can_transfer(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        self.bank.transfer(3000, 1, 2, "pin1")

        self.assertEqual(2000, self.bank.check_balance("pin1", 2))

    def test_that_account_can_transfer_with_incorrectPassword_raise_invalid_pin_exception(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            self.bank.transfer(2000, 1, 2, "pint")

    def test_that_bank_can_find_account(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.find_account(1)
        self.assertEqual(account, self.bank.find_account(1))

    def test_that_bank_can_find_account_and_can_remove_account(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.remove_account(1, "pin")
        self.assertEqual(1, self.bank.get_number_of_account())

    def test_bank_can_check_balance(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        self.assertEqual(5000, self.bank.check_balance("pin1", 2))

    def test_bank_can_check_balance_with_incorrect_pin_raise_invalid_pin_exception(self):
        account = self.bank.register_customer("senior", "dev", "pin")
        account1 = self.bank.register_customer("senior1", "dev1", "pin1")
        self.bank.deposit(5000, 2)
        with self.assertRaises(InvalidPinException):
            self.bank.check_balance("pin2", 2)
