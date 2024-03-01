from unittest import TestCase
import string

from String import Praise


class TestPraise(TestCase):
    def test_get_string(self):
        my_school = "abs"
        praise = Praise(my_school)
        self.assertEqual("abs",)
