from . import features


class GenericGeometry:
    area = features.Area()
    perimeter = features.Perimeter()


class GenericVolume(GenericGeometry):
    volume = features.Volume()


class Extrude(GenericVolume):
    def __init__(self, *args, d):
        super().__init__(*args)
        self.depth = d

