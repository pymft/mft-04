import collections

person_tuple = ("Jack", "Smith")
person_list = ["Jack", "Smith"]
person_dictionary = {"name":"Jack", "last_name": "Smith"}

class Person:
    def __init__(self, name, last):
        self.name = name
        self.last_name = last

person = Person("Jack", "Smith")


person_tuple[0]
person_list[0]
person_dictionary["name"]
person.name


Point = collections.namedtuple('Point', ['x', 'y'])
