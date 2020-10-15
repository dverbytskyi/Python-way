class Point2D:
    """Point on the plane"""

    instances_count = 0 # number of class instances

    # constructor / initializing method / special method starts with __
    def __init__(self, x, y):
        self.x = x
        self.y = y  # 'self' points to the current instance of the class

        Point2D.instances_count += 1  # increase with every class initialization

    # string representation of a class
    def __str__(self):
        return "Point 2D ({}, {})".format(self.x, self.y)  # return "string"

    # creating new object as SUM 'self' and 'other' coordinates
    def __add__(self, other):
        # check if 'self' and 'other' the same instance of current class - point and point
        if isinstance(other, self.__class__):
            return Point2D(self.x + other.x, self.y + other.y)  # return SUM object
        elif isinstance(other, (int, float)):  # point and number
            self.x += other  # move point on 'other' for x and y / self.x_y + other
            self.y += other
            return self
        else:  # raise an exception with unsupported object type
            raise TypeError("Can't add {1} and {0}".format(self.__class__, type(other)))

    # creating new object as DIFF 'self' and 'other' coordinates
    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    # invert coordinates
    def __neg__(self):
        return Point2D(-self.x, -self.y)

    # if the points are same
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # if the points are diff
    def __ne__(self, other):
        return not (self == other)

    # the distance to the center.
    def distance(self):
        return (self.x**2 + self.y**2)**0.5

    @staticmethod  # static method belongs to the class, but knows nothing about it
    def sum(*points):
        assert len(points) > 0 # check points count != 0
        res = points[0]
        for point in points[1:]:
            res += point
        return res

    @classmethod  # class method available with Point2D.from_string
    def from_string(cls, str_value):  # cls - instance to the class
        values = [float(x) for x in str_value.split(',')]
        assert len(values) == 2

        return cls(*values)


if __name__ == "__main__":
    p1 = Point2D(0, 5)
    p2 = Point2D(-5, 10)
    p3 = Point2D.from_string("5, 6")  # creating third point with class method
    p4 = Point2D.sum(p1, p2, p3, Point2D(0, -21))  # adding points via static method

    print("p1 + p2: ", p1 + p2)
    print("p1 + 2: ", p1 + 2)
    print("p1 + 5.0: ", p1 + 5.0)
    print("p1 + p3: ", p1 + p3)
    print("p4: ", p4)
    # print(p1 + "string") raise TypeError
    print("p1 + p2: ", p1 - p2)
    print("-p2: ", -p2)
    print("p1 == p2, p1 != p2: ", p1 == p2, p1 != p2)
    print("Distance to center of coordinates (p1): {:.2f}".format(p1.distance()))
    print("Distance to center of coordinates (p2): {:.2f}".format(p2.distance()))
    print("instances_count: ", Point2D.instances_count)  # count of created points via a class variable





