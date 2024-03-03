class Gun:
    def __init__(self):
        self.num_of_bullet = 0

    def get_chamber(self):
        return self.num_of_bullet

    def add_bullet(self):
        if 0 <= self.num_of_bullet < 12:
            self.num_of_bullet += 1

    def load_bullet(self):
        self.num_of_bullet = 12

    def shoot_bullet(self):
        if self.num_of_bullet > 0:
            self.num_of_bullet -= 1

    def reload_bullet(self):
        self.num_of_bullet = 12
