import functools

f = lambda a, b: a + b

lst = [2, 3, 6, 2, 1]

res = functools.reduce(f, lst)
print(res)

#
# f(2, f(3, f(6, f(2, 1))))
#
#
# (2 * (3 * (6 * (2 * 1))))
# (2 * (3 * (6 * 2)))
# (2 * (3 * 12))
# (2 * 36)
# 72
