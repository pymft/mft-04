class Fahrenheit:
    def __get__(self, instance, owner):
        return 32 + instance.celsius * 1.8

    def __set__(self, instance, value):
        instance.celsius = (5 / 9) * (value - 32)


class Temperature:
    fahrenheit = Fahrenheit()

    def __init__(self, celsius):
        self.celsius = float(celsius)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

