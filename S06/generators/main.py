import time


def fib_rec(n):
    if n in (0, 1):
        return 1
    return fib_rec(n-1) + fib_rec(n-2)


def fib_fun(n):
    if n in (0, 1):
        return n
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b

    return b


def fib_gen(n):
    a, b = 0, 1
    yield a
    yield b

    for _ in range(2, n):
        a, b = b, a + b

        yield b


n = 1000


# t_i = time.time()
# out = []
# for i in range(n):
#     out.append(fib_rec(i))
#
# t_e= time.time()
# print("elapsed time  :", t_e - t_i)


t_i = time.time()
out = []
for i in range(n):
    out.append(fib_fun(i))

t_e= time.time()
print("elapsed time  :", t_e - t_i, len(out))


t_i = time.time()
out = list(fib_gen(n))
t_e= time.time()
print("elapsed time  :", t_e - t_i, len(out))