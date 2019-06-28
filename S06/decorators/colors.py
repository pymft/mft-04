def color(color_code, font_type):
    color_map = {"red": "31", "green": "32", "purple": "35", "yellow": "33"}
    font_type_map = {"regular": 0, "bold": 1, "underline": 4, "reverse": 7}
    def decorator(f):
        def inner(*args, **kw):
            res = f"\033[{color_map[color_code]};{font_type_map[font_type]}m{f(*args, **kw)}\033[0m"
            return res

        return inner
    return decorator


@color("red", "bold")
def echo(s):
    return s


print(echo("hello"))
