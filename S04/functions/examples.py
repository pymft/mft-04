
def stars(n, pattern="*"):
    width = n * 2 - 1
    for i in range(n):
        asterisks = pattern * (2 * i + 1)
        line = asterisks.center(width)
        print(line)


stars(10)
stars(4, pattern='.')