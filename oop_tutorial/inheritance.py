class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) # inherit the age and name variable from Pet
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I am color {self.color}")


class Dog(Pet):
    def speak(self):
        print('Bark')


p = Pet('Tim', 22)
p.show()
c = Cat('Bill', 14, 'green')
c.show()
c.speak()
d = Dog('Terry', 26)
d.show()

print()
p.speak()
c.speak()
d.speak()