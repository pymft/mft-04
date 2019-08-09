import collections


d = collections.deque([1, 2, 3, 4, 5])

print(d)

d.append(6)
print(d)

d.appendleft(0)
print(d)

d.rotate(2)
print(d)