def fact(n):
    if n == 0:
        return 1
    res = n * fact(n-1)
    return res


fact(5)