lst = [90, 55, 32, 63, 100]
#
# for i, n in enumerate(lst):
#     print(i, n)

a = [10, 20, 30, 40, 50, 60]
b = [11, 22, 33, 44, 55, 66]
c = [101, 202, 303, 404, 505, 606]
#
# for i in range(len(a)):
#     print(a[i], b[i], c[i])

# print(list(zip(a, b)))

for x, y, z in zip(a, b, c):
    print(x, y, z)
