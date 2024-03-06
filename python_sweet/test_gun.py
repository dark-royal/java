import unittest

from python_sweet.Gun import Gun
from python_sweet.bullet_overloaded_exception import BulletOverLoadedException
from python_sweet.invalid_pin_exception import InvalidPinException
from python_sweet.no_bullet_found_exception import NoBulletFoundException


class MyTestCase(unittest.TestCase):
    def test_gun_is_empty(self):
        my_gun = Gun(1234)
        self.assertTrue(my_gun.is_empty())

    def test_that_number_of_bullet_can_add_bullet_with_valid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        self.assertEqual(1,my_gun.get_chamber())

    def test_gun_can_add_three_bullet_with_valid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        self.assertEqual(3, my_gun.get_chamber())

    def test_gun_can_shoot_gun_with_valid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        my_gun.shoot_bullet(1234)
        self.assertEqual(2,my_gun.get_chamber())

    def test_gun_cannot_shoot_gun_while_there_is_no_bullet_in_the_gun(self):
        my_gun = Gun(1234)
        with self.assertRaises(NoBulletFoundException):
            my_gun.shoot_bullet(1234)

    def test_gun_cannot_add_more_than_5_bullet_with_valid_pin(self):
        my_gun = Gun(1234)
        with self.assertRaises(BulletOverLoadedException):
            my_gun.add_bullet(1234)
            my_gun.add_bullet(1234)
            my_gun.add_bullet(1234)
            my_gun.add_bullet(1234)
            my_gun.add_bullet(1234)
            my_gun.add_bullet(1234)

    def test_that_gun_can_reload_gun_with_valid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        my_gun.shoot_bullet(1234)
        my_gun.shoot_bullet(1234)
        my_gun.reload_bullet(1234)
        self.assertEqual(5,my_gun.get_chamber())

    def test_that_gun_cannot_reload_more_than_the_bullet_size_raise_bullet_overloaded_with_valid_pin(self):
        my_gun = Gun(1234)
        with self.assertRaises(BulletOverLoadedException):
            my_gun.reload_bullet(1234)
            my_gun.reload_bullet(1234)

    def test_gun_can_load_gun_with_valid_pin(self):
        my_gun = Gun(1234)
        my_gun.load_bullet(1234)
        self.assertEqual(1,my_gun.get_chamber())

    def test_gun_cannot_add_bullet_with_invalid_pin(self):
        my_gun = Gun(1234)
        with self.assertRaises(InvalidPinException):
            my_gun.add_bullet(1111)

    def test_gun_cannot_shoot_gun_with_invalid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        with self.assertRaises(InvalidPinException):
            my_gun.shoot_bullet(1111)
        self.assertEqual(1,my_gun.get_chamber())

    def test_gun_cannot_reload_gun_with_invalid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        my_gun.shoot_bullet(1234)
        with self.assertRaises(InvalidPinException):
            my_gun.reload_bullet(2345)
        self.assertEqual(0,my_gun.get_chamber())

    def test_gun_cannot_load_gun_with_invalid_pin(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        my_gun.add_bullet(1234)
        my_gun.shoot_bullet(1234)
        with self.assertRaises(InvalidPinException):
            my_gun.load_bullet(1243)
        self.assertEqual(1,my_gun.get_chamber())

    # def test_gun_cannot_perform_any_operation_when_the_gun_is_empty_raise_exception(self):
    #     my_gun = Gun(1234)
    #     with self.assertRaises(BaseException):
    #         my_gun.shoot_bullet(1234)
    #         my_gun.load_bullet(1234)
    #         my_gun.reload_bullet(1234)
    #     #self.assertTrue(my_gun.is_empty())
    #
    def test_gun_cannot_reload_when_the_gun_is_not_empty(self):
        my_gun = Gun(1234)
        my_gun.add_bullet(1234)
        with self.assertRaises(BulletOverLoadedException):
            my_gun.reload_bullet(1234)










