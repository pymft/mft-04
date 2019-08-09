import math

from . import consts
from . import shapes
PI = consts.PI


class Area:
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Paralleogram):
            angle = math.radians(instance.alpha)
            coef = math.sin(angle)
            return instance.a * instance.b * coef

        elif isinstance(instance, shapes.Circle):
            return PI * instance.radius ** 2

    def __set__(self, instance, value):
        ratio = value / instance.area
        ratio = ratio ** 0.5
        if isinstance(instance, shapes.Paralleogram):
            instance.a *= ratio
            instance.b *= ratio
        elif isinstance(instance, shapes.Circle):
            instance.radius *= ratio


class Perimeter:
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Paralleogram):
            return 2 * (instance.a + instance.b)
        elif isinstance(instance, shapes.Circle):
            return 2 * PI * instance.radius

    def __set__(self, instance, value):
        ratio = value / instance.perimeter
        if isinstance(instance, shapes.Paralleogram):
            instance.a *= ratio
            instance.b *= ratio
        elif isinstance(instance, shapes.Circle):
            instance.radius *= ratio


class Volume:
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Extrude):
            return instance.area * instance.depth

        elif isinstance(instance, shapes.Sphere):
            return 2/3 * instance.area * instance.radius