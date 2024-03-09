from unittest import TestCase

from diary_package import diaries
from diary_package.diaries import Diaries
from diary_package.no_diary_is_found_exception import NoSuchDiaryExistException


class TestDiary(TestCase):

    def setUp(self):
        self.dairies = Diaries()

    def test_add_diary(self):
        self.dairies.add_diary("username", "password")
        self.assertEqual(1, self.dairies.get_number_of_diaries())

    def test_diaries_can_add_two_diaries(self):
        self.dairies.add_diary("username", "password")
        self.dairies.add_diary("username1", "password1")
        self.assertEqual(2, self.dairies.get_number_of_diaries())

    def test_diaries_can_find_diary_with_user_name(self):
        self.dairies.add_diary("username", "password")
        self.dairies.add_diary("username1", "password1")
        found_diary = self.dairies.find_by_user_name("username")
        self.assertEqual(found_diary, self.dairies.find_by_user_name("username"))

    def test__diaries_can_find_diary_with_user_name_with_incorrect_username(self):
        self.dairies.add_diary("username", "password")
        self.dairies.add_diary("username1", "password1")
        with self.assertRaises(NoSuchDiaryExistException):
            self.dairies.find_by_user_name("usernime")

    def test_diaries_can_delete_diary_from_diaries(self):
        self.dairies.add_diary("username", "password")
        self.dairies.add_diary("username1", "password1")
        self.assertEqual(2, self.dairies.get_number_of_diaries())
        self.dairies.delete_diary("username", "password")
        self.assertEqual(1, self.dairies.get_number_of_diaries())

    def test_diaries_can_delete_diary_from_diaries_with_incorrect_username_throw_no_such_diary_exist_exception(self):
        self.dairies.add_diary("username", "password")
        self.dairies.add_diary("username1", "password1")
        self.assertEqual(2, self.dairies.get_number_of_diaries())
        with self.assertRaises(NoSuchDiaryExistException):
            self.dairies.delete_diary("usernime", "passwors")

           

