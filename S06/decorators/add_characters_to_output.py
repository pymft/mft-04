def add_stars(f):
    def inner(*args, **kwargs):
        return "*" + f(*args, **kwargs) + "*"

    return inner


@add_stars
def echo(a):
    return a


@add_stars
def rev(a):
    return a[::-1]


res = echo("hello")
print(res)
