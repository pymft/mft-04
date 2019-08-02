# syntax error
# runtime error
# logical error

a = 1
b = 0
lst = [1, 2, 3]
dct = {'one': 1000}
try:
    c = a / b
    print(c)
    print(dct['two'])
except ZeroDivisionError as e:
    print("something went wrong! zero division err")
except LookupError as e:
    print("invalid index or key")
finally: