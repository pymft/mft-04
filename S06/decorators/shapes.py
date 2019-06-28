def shape_decorator_maker(shape):
    def decorator(f):
        def inner(*args, **kw):
            res = f(*args, **kw)
            res = shape + res + shape
            return res

        return inner
    return decorator


# decor1 = shape_decorator_maker("@")
# decor2 = shape_decorator_maker("#")
# decor3 = shape_decorator_maker("*")


@shape_decorator_maker("%")
@shape_decorator_maker("$")
@shape_decorator_maker("@")
def echo(s):
    return s


print(echo("hello"))
