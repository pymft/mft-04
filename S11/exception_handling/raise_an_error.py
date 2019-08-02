class InvalidTriangleError(ValueError):
    pass


class InvalidTypeOfTriangleSidesError(TypeError):
    pass


def is_triangle(a, b, c) -> bool:
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        raise InvalidTypeOfTriangleSidesError
    return a + b > c and a + c > b and b + c > a


def type_of_triangle(a: int, b: int, c: int):
    if not is_triangle(a, b, c):
        raise InvalidTriangleError

    map_types = {1: "Equilateral", 2: "Isosceles", 3: "Inequilateral"}
    temp = len({a, b, c})

    return map_types[temp]


try:
    res = type_of_triangle(9, 9, 9)
    print(res)
except InvalidTriangleError:
    print("invalid triangle")

except InvalidTypeOfTriangleSidesError:
    print("all sides must be int")
