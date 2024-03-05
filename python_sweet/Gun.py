from python_sweet.bullet_overloaded_exception import BulletOverLoadedException
from python_sweet.no_bullet_found_exception import NoBulletFoundException


class Gun:
    def __init__(self):
        self.num_of_bullet = 0

    def get_chamber(self):
        return self.num_of_bullet

    def add_bullet(self):
        if 5 > self.num_of_bullet >= 0:
            self.num_of_bullet += 1
        else:
            raise BulletOverLoadedException("Bullet should be 5")

    def load_bullet(self):
        if 5 > self.num_of_bullet >= 0:
            self.num_of_bullet += 1
            return self.num_of_bullet
        raise BulletOverLoadedException("bullet capacity is 5")

    def shoot_bullet(self):
        if self.is_empty():
            raise NoBulletFoundException("chamber is empty!!, add bullet")

        else:
            if self.num_of_bullet > 0:
                self.num_of_bullet -= 1

    def reload_bullet(self):
        if self.num_of_bullet == 0:
            self.num_of_bullet = 5
            return self.num_of_bullet
        raise BulletOverLoadedException("Gun is overloaded")

    def is_empty(self):
        return self.num_of_bullet == 0
