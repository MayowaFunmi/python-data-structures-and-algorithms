class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print('bark')

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age


d = Dog('Tim', 43)
d.bark()
print(d.add_one(7))
print(d.get_age())
d.set_age(12)
print(d.get_age())
print(d.age)