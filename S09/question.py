def flatten(inp):
    if isinstance(inp, int):
        return [inp]
    elif isinstance(inp, list):
        res = []
        for member in inp:
            res.extend(flatten(member))
        return res

# print(flatten(1))

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
inp = [1, [[2, 3], [[[4], 5], [6, 7], 8], 9], 10]
print(flatten(inp))
