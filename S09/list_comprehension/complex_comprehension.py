def is_even(n):
    return n % 2 == 0


def f(n):
    res = 0 if n < 5 else n ** 2
    return res


inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# out = [f(i) for i in inp if is_even(i)]

out = [0 if i < 5 else i ** 2 for i in inp if i % 2 == 0]

print(out)
