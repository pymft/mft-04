import math
import time

out = 0
i = 1
epsilon = 10e-12

t1 = time.time()

out_expected = math.pi ** 4 / 90

while True:
    out = out + 1/i**4
    err = abs(out_expected - out)/out_expected
    if err < epsilon:
        break
    i += 1

pi_computed = math.sqrt(math.sqrt(out*90))
t2 = time.time()
print("Elapsed time = ", (t2-t1)*1000, " (ms)")
print(pi_computed)
print(math.pi)
print("iterations = ", i)
