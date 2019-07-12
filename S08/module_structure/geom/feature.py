import math

from . import shapes


class BaseFeatureSetter:
    def set_vals(self, instance, ratio):
        if isinstance(instance, shapes.Rectangle):
            instance.width *= ratio
            instance.height *= ratio

        elif isinstance(instance, shapes.Circle):
            instance.radius *= ratio


class Area(BaseFeatureSetter):
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Rectangle):
            return instance.width * instance.height
        elif isinstance(instance, shapes.Circle):
            return instance.radius ** 2 * math.pi

    def __set__(self, instance, value):
        ratio = math.sqrt(value / instance.area)
        self.set_vals(instance, ratio)


class Perimeter(BaseFeatureSetter):
    def __get__(self, instance, owner):
        if isinstance(instance, shapes.Rectangle):
            return (instance.width + instance.height) * 2
        elif isinstance(instance, shapes.Circle):
            return instance.radius * 2 * math.pi

    def __set__(self, instance, value):
        ratio = value / instance.perimeter
        self.set_vals(instance, ratio)
