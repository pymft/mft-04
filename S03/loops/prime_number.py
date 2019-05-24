import math

number = 73939133

i = 2
is_prime = True

while i**2 < number:
    if number % i == 0:
        is_prime = False
        break

    i = i + 1

print(i)
print(is_prime)

# 1  (2) ---------------------------------------------(n-1)  n
