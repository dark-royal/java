import unittest

from bank_account.Account import Account
from bank_account.Exception import InvalidAmountException


class MyTestCase(unittest.TestCase):

    def test_deposit_amount(self):
        account = Account("praise", "1111", 1)
        with self.assertRaises(InvalidAmountException):
            account.deposit(-2000)

    def test_deposit_positive_amount(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(2000)
        self.assertEqual(2000, account.get_balance())

    def test_deposit_2k_and_5k_balance_is_7k(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(2000)
        account.deposit(5000)
        self.assertEqual(7000, account.get_balance())

    def test_deposit_5k_withdraw_2k_balance_is_3k(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(5000)
        account.withdraw(2000,1111)
        self.assertEqual(3000, account.get_balance())

    def test_deposit_5k_withdraw_2k_with_invalid_pin_balance_is_5k(self):
        account = Account("praise","1111",1)
        self.assertEqual(0,account.get_balance())
        account.deposit(5000)
        account.withdraw(2000,"1212")
        self.assertEqual(5000,account.get_balance())
