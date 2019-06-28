# print(1, 2, 3, 4, 5, sep='----')

f = print
args = (1, 2, 3, 4, 5)
kwars = {'sep': '----'}

f(*args, **kwars)
