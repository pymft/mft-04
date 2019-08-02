import math


class Rectangle:
    """
    >>> r = Rectangle(2.0, 5.0)
    >>> r.area
    10.0
    >>> r.area = 40.0
    >>> (r.width, r.height)
    (4.0, 10.0)
    >>> r.perimeter = 14.0
    >>> (r.width, r.height)
    (2.0, 5.0)
    """

    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio = math.sqrt(value / self.area)
        self.width *= ratio
        self.height *= ratio

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

    @perimeter.setter
    def perimeter(self, value):
        ratio = value / self.perimeter
        self.width *= ratio
        self.height *= ratio


if __name__ == '__main__':
    import doctest

    doctest.testmod()
