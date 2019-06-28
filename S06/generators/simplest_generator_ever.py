def my_simple_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6
    yield 7
    yield 8
    yield 9
    yield 10


gen1 = my_simple_generator()

for i in gen1:
    print(i)
