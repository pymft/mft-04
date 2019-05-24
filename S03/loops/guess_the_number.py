import random


secret = random.randint(1, 100)

while True:
    answer = input("guess the secret number: ")
    num = int(answer)

    if num > secret:
        print("number is greater than secret ")
    elif num < secret:
        print("number is lesser than secret ")
    elif num == secret:
        print("Bingo")
        break

