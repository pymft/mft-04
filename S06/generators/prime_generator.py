from math import sqrt
import time


def is_prime(n):
    limit = int(sqrt(n)) + 1
    # limit = n
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


def prime_generator(n):
    i = 1
    count = 0
    while count < n:
        i += 1
        if is_prime(i):
            count += 1
            yield i



t_i = time.time()
res = list(prime_generator(100))
t_e= time.time()
print("elapsed time  :", t_e - t_i, len(res))


for i in prime_generator(1000):
    print(i)