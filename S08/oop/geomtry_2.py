import math

class Area:
    def __get__(self, instance, owner):
        if owner == Rectangle:
            return instance.width * instance.height
        elif owner == Circle:
            return instance.radius ** 2 * math.pi

    def __set__(self, instance, value):
        # if type(instance) == Rectangle:
        ratio = math.sqrt(value / instance.area)
        if isinstance(instance, Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, Circle):
            instance.radius *= ratio


class Rectangle:
    area = Area()

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h


class Circle:
    area = Area()

    def __init__(self, r: float):
        self.radius = r



if __name__ == '__main__':
    r = Rectangle(5.0, 6.0)
    print(r.width, r.height, r.area)  # 30.0
    r.area = 120.0
    print(r.width, r.height, r.area)  # 30.0
    c = Circle(10)
    print(c.radius, c.area)
    c.area = c.area * 4
    print(c.radius, c.area)
