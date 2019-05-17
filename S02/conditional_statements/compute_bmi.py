weight = float(input("Weight (kg) : "))
height = float(input("Height (m) : "))

bmi = weight / (height * height)

print(bmi)

if bmi < 18:
    print("under-weight")
elif bmi < 25:
    print("Normal!")
else:
    print("over-weight")
