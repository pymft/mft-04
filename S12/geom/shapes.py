from . import base


class Circle(base.GenericGeometry):
    def __init__(self, r):
        self.radius = r


class Paralleogram(base.GenericGeometry):
    def __init__(self, a, b, alpha):
        self.a = a
        self.b = b
        self.alpha = alpha


class Rectangle(Paralleogram):
    def __init__(self, w, h):
        super().__init__(w, h, 90)

    @property
    def width(self):
        return self.a

    @property
    def height(self):
        return self.b


class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)

    @property
    def side(self):
        return self.width

