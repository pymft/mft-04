import math


class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, Rectangle):
            return instance.width * instance.height
        elif isinstance(instance, Circle):
            return instance.radius ** 2 * math.pi

    def __set__(self, instance, value):
        ratio = math.sqrt(value / instance.area)
        if isinstance(instance, Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, Circle):
            instance.radius *= ratio


class Perimeter:
    def __get__(self, instance, owner):
        if isinstance(instance, Rectangle):
            return (instance.width + instance.height) * 2
        elif isinstance(instance, Circle):
            return instance.radius * 2 * math.pi

    def __set__(self, instance, value):
        ratio = value / instance.perimeter
        if isinstance(instance, Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, Circle):
            instance.radius *= ratio


class Geometry:
    area = Area()
    perimeter = Perimeter()


class Rectangle(Geometry):
    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h


class Square(Rectangle):
    def __init__(self, a: float):
        super().__init__(a, a)


class Circle(Geometry):
    def __init__(self, r: float):
        self.radius = r



if __name__ == '__main__':
    r = Square(5.0)
    print(r.width, r.height, r.area, r.perimeter)  # 30.0
    r.area = 120.0
    print(r.width, r.height, r.area, r.perimeter)  # 30.0
    r.perimeter *= 2
    print(r.width, r.height, r.area, r.perimeter)  # 30.0
    c = Circle(10)
    print(c.radius, c.area, c.perimeter)
    c.area = c.area * 4
    print(c.radius, c.area, c.perimeter)
    c.perimeter *= 2
    print(c.radius, c.area, c.perimeter)
