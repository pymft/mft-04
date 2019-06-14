
def factorial(num):
    """ compute factorial for number ``num``    """
    res = 1
    for i in range(1, num+1):
        res = res * i
    return res


def combination(m, n):
    a = factorial(m)
    b = factorial(n) * factorial(m-n)
    res = a // b
    return res


def pascal_row(row_number):
    out = []
    for i in range(row_number+1):
        out.append(combination(row_number, i))

    return out


def full_pascal(n):
    res = []
    for i in range(n):
        tmp = pascal_row(i)
        res.append(tmp)

    return res


print(full_pascal(10))


factorial()
