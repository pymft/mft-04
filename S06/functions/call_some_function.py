# print(1, 2, 3, 4, 5, sep='----')

def call_it(f, args, kwargs):
    return f(*args, **kwargs)

f = print
args = (1, 2, 3, 4, 5)
kwargs = {'sep': '----'}

call_it(f, args, kwargs)
