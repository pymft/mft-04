import math
import time


out = 0
limit = 10000
out = 0

for i in range(1, limit+1):
    out = out + 1/i**2

print(math.sqrt(out*6))

