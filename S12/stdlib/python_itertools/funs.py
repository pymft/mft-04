import itertools

f = lambda r: ''.join(r)

res =  itertools.permutations("abcde", 3)

out = [f(r) for r in res]
print(out)
