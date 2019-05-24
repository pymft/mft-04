lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
rng = range(0, 20)
rng_lst = list(rng)
print(type(rng))
print(lst)
print(rng, rng.__sizeof__())
print(rng_lst, rng_lst.__sizeof__())