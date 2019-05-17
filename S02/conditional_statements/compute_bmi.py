weight = int(input("enter weight (kg) : "))
height = 1.8

bmi = weight / (height * height)

print(bmi)
bmi = 17

if bmi <= 18:
    print("under-weight")
elif bmi >= 25:
    print("Normal!")
else:
    print("over-weight")
