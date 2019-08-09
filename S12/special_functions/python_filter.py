f = lambda x: x % 2 == 0

lst = [1, 2, 3, 4, 5, 6]
out = [i for i in lst if f(i)]

out = filter(f, lst)
out = list(out)
print(out)