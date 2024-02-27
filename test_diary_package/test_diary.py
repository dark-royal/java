import unittest

from diary_package import diary


class MytestCase(unittest.TestCase):
    def test_diary_can_lock(self):
        my_diary = diary.Diary("user name", "password")
        my_diary.lock_diary()
        self.assertTrue(my_diary.is_locked)

    def test_that_diary_can_unlock(self):
        my_diary = diary.Diary("user_name","password")
        my_diary.unlock("password")
        self.assertTrue(my_diary.is_locked)

    def test_can_create_entry(self):
        my_diary = diary.Diary("user name","password")
        my_diary.create_entry("title","body",1)
        self.assertEqual(1,my_diary.get_number_of_entry())
