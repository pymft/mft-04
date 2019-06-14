f = open('input.txt', mode='r')
print(f)
text = f.read(4)
print(text)
text = f.read(4)
print(text)
text = f.read()
print(text)

f.close()


