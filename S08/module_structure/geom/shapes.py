from . import base


class Rectangle(base.Geometry):
    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h


class Square(Rectangle):
    def __init__(self, a: float):
        super().__init__(a, a)


class Circle(base.Geometry):
    def __init__(self, r: float):
        self.radius = r
