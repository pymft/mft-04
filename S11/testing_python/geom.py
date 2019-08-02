import math


class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, value):
        self.check_value_type(value)
        ratio = math.sqrt(value / self.area)
        self.change_ratio(ratio)

    @property
    def perimeter(self):
        return (self.width + self.height) * 2

    @perimeter.setter
    def perimeter(self, value):
        self.check_value_type(value)
        ratio = value / self.perimeter
        self.change_ratio(ratio)

    def check_value_type(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError

    def change_ratio(self, ratio):
        self.width *= ratio
        self.height *= ratio
