import math

number = 73939133


is_prime = True
limit = int(math.sqrt(number))+1

for i in range(2, limit):
    if number % i == 0:
        is_prime = False
        break


print(number, is_prime, i)
