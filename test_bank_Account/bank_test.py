import unittest


class MyTestCase(unittest.TestCase):


    def test_account_can_register_account(self):
        bank = Bank()
        account = bank.register_customer("")
