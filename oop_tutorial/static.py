class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1


p1 = Person('Ade')
print(p1.number_of_people)
p2 = Person('Bello')
print(p2.number_of_people)
print(Person.number_of_people)
