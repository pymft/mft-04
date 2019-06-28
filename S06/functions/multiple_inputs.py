def my_sum(*args, **kwargs):
    print(args)
    print(kwargs)


my_sum(1, 2, 3, whatever="hello")
my_sum(1, 2, 3, 3, 2, 3, mode="what?")
my_sum(1, a=1, b=2, c=100)


