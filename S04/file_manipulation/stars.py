with open('input.txt', mode='r') as fr:
    text = fr.read()
    num, c = text.split('\n')
    num = int(num)

# res = ''
# for i in range(num):
#     res += (c + ' ') * num + '\n'

line = (c + ' ') * num
res = '\n'.join([line for _ in range(num)])

with open('output.txt', mode='w') as fw:
    fw.write(res)