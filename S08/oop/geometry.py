class Rectangle:
    """
    Creates a rectangle object.

    Examples
    --------
    >>> r = Rectangle(5.0, 6.0)
    >>> r.width, r.height, r.area, r.perimeter
    (5.0, 6.0, 30.0, 22.0)
    >>> r.area = 120.0
    >>> r.width, r.height
    (10.0, 12.0)
    >>> r.perimeter
    44.0
    """

    def __init__(self, w: float, h: float):
        self.width = w
        self.height = h

    @property
    def area(self) -> float:
        return self.width * self.height

    @area.setter
    def area(self, value: float):
        ratio = (value / self.area) ** 0.5
        self.width *= ratio
        self.height *= ratio

    @property
    def perimeter(self) -> float:
        return (self.width + self.height) * 2

    @perimeter.setter
    def perimeter(self, value: float):
        ratio = value / self.perimeter
        self.width *= ratio
        self.height *= ratio


if __name__ == '__main__':
    import doctest

    doctest.testmod()
