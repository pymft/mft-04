import math


limit = 1000
out = 0
i = 0

while i < limit:
    i = i + 1
    out = out + 1/i**4

pi_approximate = math.sqrt(math.sqrt(out*90))
print(pi_approximate)
print(math.pi)
