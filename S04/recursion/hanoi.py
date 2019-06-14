def hanoi(n, start, middle, target):
    if n == 1:
        print(start, '-->', target)
    else:
        hanoi(n - 1, start, target, middle)
        hanoi(1, start, middle, target)
        hanoi(n - 1, middle, start, target)


hanoi(3, 'A', 'B', 'C')
