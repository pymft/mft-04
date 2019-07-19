class InnerClass:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return self.name
        # print("self", self)
        # print("sample", instance)
        # print("Something", owner)


class Something:
    a_class_var = InnerClass("??????")

    def __init__(self, a):
        self.a = a

    @property
    def a_2(self):
        return self.a * self.a


sample = Something(10)

print(sample.a_class_var)
print( Something.a_class_var)

