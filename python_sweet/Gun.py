from python_sweet.bullet_overloaded_exception import BulletOverLoadedException
from python_sweet.invalid_pin_exception import InvalidPinException
from python_sweet.no_bullet_found_exception import NoBulletFoundException


class Gun:
    def __init__(self,pin):
        self.num_of_bullet = 0
        self.pin = pin

    def get_chamber(self):
        return self.num_of_bullet

    def add_bullet(self,pin):
        self.validate_pin(pin)
        if 5 > self.num_of_bullet >= 0:
            self.num_of_bullet += 1
        else:
            raise BulletOverLoadedException("Bullet should be 5")

    def load_bullet(self,pin):
        self.validate_pin(pin)
        if 5 > self.num_of_bullet >= 0:
            self.num_of_bullet += 1
            return self.num_of_bullet
        raise BulletOverLoadedException("bullet capacity is 5")

    def shoot_bullet(self,pin):
        self.validate_pin(pin)
        if self.is_empty():
            raise NoBulletFoundException("chamber is empty!!, add bullet")

        else:
            if self.num_of_bullet > 0:
                self.num_of_bullet -= 1

    def reload_bullet(self,pin):
        self.validate_pin(pin)
        if self.num_of_bullet == 0:
            self.num_of_bullet = 5
            return self.num_of_bullet
        raise BulletOverLoadedException("Gun is overloaded")

    def is_empty(self):
        return self.num_of_bullet == 0

    def validate_pin(self,pin):
        if self.pin != pin:
            raise InvalidPinException("incorrect pin")
        return pin

