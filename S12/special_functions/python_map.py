f = lambda x: x ** 2

lst = [1, 2, 3, 4, 5, 6]
# out = [f(i) for i in lst]

out = map(f, lst)

print(list(out))

# print(out)
