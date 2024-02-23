import unittest

from bank_account.Account import Account


class MyTestCase(unittest.TestCase):

    def test_deposit_negative_amount(self):
        account = Account("praise", "1111", 1)
        with self.assertRaises(Exception):
            account.deposit(-2000)

    def test_deposit_zero_raise_invalid_amount_exception(self):
        account = Account("praise", "1111", 1)
        with self.assertRaises(Exception):
            account.deposit(0)

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
        account.withdraw(2000, "1111")
        self.assertEqual(3000, account.get_balance())

    def test_deposit_5k_withdraw_2k_with_invalid_pin_balance_is_5k(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(5000)
        with self.assertRaises(Exception):
            account.withdraw(2000, "1212")
        self.assertEqual(5000, account.get_balance())

    def test_deposit_5k_withdraw_negative_amount_raise_invalid_amount_exception(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(5000)
        with self.assertRaises(Exception):
            account.withdraw(-2000, "1111")
            self.assertEqual(5000, account.get_balance())

    def test_deposit_6k_withdraw_7k_raise_insufficient_funds(self):
        account = Account("praise", "1111", 1)
        self.assertEqual(0, account.get_balance())
        account.deposit(6000)
        with self.assertRaises(Exception):
            account.withdraw(7000, "1111")
            self.assertEqual(6000, account.get_balance())
