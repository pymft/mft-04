inp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# out = []
# for i in inp:
#     if i % 2 == 0:
#         out.append(i ** 2)

out = [i ** 2 for i in inp if i % 2 == 0]

# [f(i) for i in lst if cond(i)]
print(out)
