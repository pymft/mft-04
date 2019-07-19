class Sample:
    instances = {}

    def __new__(cls, *args, **kwargs):
        name = args[0]

        if name not in cls.instances:
            cls.instances[name] = super().__new__(cls)

        return cls.instances[name]

    def __init__(self, name):
        self.name = name


lst = []

for i in range(5):
    lst.append(Sample("Jack"))

lst.append(Sample("John"))

print(lst)