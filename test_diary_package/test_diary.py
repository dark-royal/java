import unittest

from diary_package import diary
from diary_package.diary import Diary
from diary_package.diary_is_locked_exception import DiaryIsLockedException
from diary_package.invalid_pin_exception import InvalidPinException, InvalidPinException


class MytestCase(unittest.TestCase):

    def setUp(self):
        self.my_diary = Diary("username", "password")

    def test_diary_can_lock(self):
        self.my_diary.lock_diary()
        self.assertTrue(self.my_diary.is_locked)

    def test_that_diary_can_unlock(self):
        self.my_diary.unlock("password")
        self.assertTrue(self.my_diary.is_locked)

    def test_that_diary_is_unlocked_with_incorrect_pin_raise_invalid_pin_exception(self):
        with self.assertRaises(InvalidPinException):
            self.my_diary.unlock("invalid password")

    def test_can_create_entry(self):
        self.assertRaises(DiaryIsLockedException, lambda: self.my_diary.create_entry("title", "body", 1))
        self.assertEqual(0, self.my_diary.get_number_of_entry())

    def test_that_diary_can_delete_entry(self):
        self.my_diary.unlock("password")
        self.my_diary.create_entry("title", "body", 1)
        found_entry = self.my_diary.find_entry_by_id(1)
        self.my_diary.delete_entry(found_entry)

    #  self.assertEqual(0, self.my_diary.get_number_of_entry())

    def test_that_diary_can_find_entry(self):
        self.my_diary.unlock("password")
        praise = self.my_diary.create_entry("title", "body", 1)
        self.assertEqual(self.my_diary.find_entry_by_id(1), praise)

    def test_diary_cannot_create_entry_while_the_diary_is_locked(self):
        self.my_diary.lock_diary()
        self.assertTrue(self.my_diary.is_locked)

    def test_that_diary_can_create_two_entry_and_find_entry_1(self):
        pass
