class Temperature:
    """
    Examples
    --------
    >>> t = Temperature(27)
    >>> t.cels
    27.0
    >>> t.fahr
    80.6
    >>> t.fahr = 100
    >>> t.cels
    37.77777777777778
    """
    def __init__(self, cels):
        self.cels = float(cels)

    @property
    def fahr(self):
        return 1.8 * self.cels + 32

    @fahr.setter
    def fahr(self, value):
        self.cels = (5/9) * (value - 32)


if __name__ == '__main__':
    import doctest

    doctest.testmod()


