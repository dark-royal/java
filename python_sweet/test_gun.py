import unittest

from python_sweet.Gun import Gun
from python_sweet.bullet_overloaded_exception import BulletOverLoadedException
from python_sweet.no_bullet_found_exception import NoBulletFoundException


class MyTestCase(unittest.TestCase):
    def test_gun_is_empty(self):
        my_gun = Gun()
        self.assertTrue(my_gun.is_empty())

    def test_that_number_of_bullet_can_add_bullet(self):
        my_gun = Gun()
        my_gun.add_bullet()
        self.assertEqual(1,my_gun.get_chamber())

    def test_gun_can_add_three_bullet(self):
        my_gun = Gun()
        my_gun.add_bullet()
        my_gun.add_bullet()
        my_gun.add_bullet()
        self.assertEqual(3, my_gun.get_chamber())

    def test_gun_can_shoot_gun(self):
        my_gun = Gun()
        my_gun.add_bullet()
        my_gun.add_bullet()
        my_gun.add_bullet()
        my_gun.shoot_bullet()
        self.assertEqual(2,my_gun.get_chamber())

    def test_gun_cannot_shoot_gun_while_there_is_no_bullet_in_the_gun(self):
        my_gun = Gun()
        with self.assertRaises(NoBulletFoundException):
            my_gun.shoot_bullet()

    def test_gun_cannot_add_more_than_5_bullet(self):
        my_gun = Gun()
        with self.assertRaises(BulletOverLoadedException):
            my_gun.add_bullet()
            my_gun.add_bullet()
            my_gun.add_bullet()
            my_gun.add_bullet()
            my_gun.add_bullet()
            my_gun.add_bullet()

    def test_that_gun_can_reload_gun(self):
        my_gun = Gun()
        my_gun.add_bullet()
        my_gun.add_bullet()
        my_gun.shoot_bullet()
        my_gun.shoot_bullet()
        my_gun.reload_bullet()
        self.assertEqual(5,my_gun.get_chamber())

    def test_that_gun_cannot_reload_more_than_the_bullet_size_raise_bullet_overloaded(self):
        my_gun = Gun()
        with self.assertRaises(BulletOverLoadedException):
            my_gun.reload_bullet()
            my_gun.reload_bullet()

    def test_gun_can_load_gun(self):
        my_gun = Gun()
        my_gun.load_bullet()
        self.assertEqual(1,my_gun.get_chamber())








