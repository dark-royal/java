class Gun:
    def __init__(self, capacity):
        self.capacity = capacity
        num_of_bullet = 0



    def add_bullet(self, num_of_bullet):
        if num_of_bullet > 12:
            raise OverflowError("bullet is more than the bullet capacity")
        else:
            self.capacity += num_of_bullet
