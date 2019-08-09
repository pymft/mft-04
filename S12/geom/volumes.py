from . import shapes
from . import base


class Cuboid(shapes.Rectangle, base.Extrude):
    pass


class Cube(shapes.Square, base.Extrude):
    pass


class Cylinder(shapes.Circle, base.Extrude):
    pass


class Sphere(shapes.Circle, base.GenericVolume):
    pass
