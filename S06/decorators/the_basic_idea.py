import time
from math import sqrt


def decorator(f):
    def decorated(*args, **kwargs):
        t1 = time.time()
        out = f(*args, **kwargs)
        t2 = time.time()
        print("elapsed time = ", t2-t1)
        return out
    return decorated


@decorator
def is_prime(n):
    limit = n
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True

@decorator
def echo(a):
    return a
# is_prime = decorator(is_prime)


print(echo("hello"))
print(is_prime(1398269))

