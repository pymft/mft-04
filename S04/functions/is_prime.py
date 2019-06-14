import math

def is_prime(number):
    i = 2

    while i < math.sqrt(number):
        if number % i == 0:
            return False

    return True


res = is_prime(73939133)
print(res)
