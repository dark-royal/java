class Complex:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    # def __add__(self, other):
    #     return Complex(self.left + other.left, self.right + other.left)

    def __sub__(self, other):
        return Complex(self.left - other.left, self.right - other.left)

    def __repr__(self):
        return f'{self.left}j{"+" if self.right > 0 else "-"} {abs(self.right)}i'

    def __gt__(self, other):
        return self.left > other.left, self.right > other.right

    def __truediv__(self, other):
        return self.left / other.left, self.right / other.right

    def __iadd__(self, other):
        return Complex(self.left + other.left, self.right + other.right)

    def __eq__(self, other):
        return self.left == other.left and self.left == other.left

    def __floordiv__(self, other):
        return Complex(self.left / other.left, self.right / other.right)


# c1 = Complex(2, 3)
# c2 = Complex(5, -2)
# c1 += c2
# print(c1)

# print(c2)
# print(c1 + c2)
# print(c1 - c2)
# print(c1 == c2)
# print(c1 > c2)
# print(c1 < c2)
# print(c2 / c2)
