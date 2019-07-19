num = 13

if num % 3 == 0:
    value = 10000
else:
    if num % 3 == 1:
        value = 100
    else:
        value = 0


cond1 = num % 3 == 0
cond2 = num % 3 == 1


# value = 1000  if cond  else 0
value = 10000 if cond1 else (100 if cond2 else 0)
