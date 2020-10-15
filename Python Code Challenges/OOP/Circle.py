import math


class Circle:

    def __init__(self, x=0, y=0, r=0):
        self.x = x
        self.y = y
        self.r = r

    def length(self):
        return 2 * math.pi * self.r

    def square(self):
        return math.pi * self.r ** 2

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, r):
        assert r > 0, "Radius must be positive"
        self._r = r

    def __str__(self):
        return "Circle ({0.x}; {0.y}) radius={0.r}".format(self)


if __name__ == "__main__":
    c = Circle(3, 4, 1)
    c.r *= 5
    print(c)
    print(c.length(), c.square())
    # c.r = -1  # assert
