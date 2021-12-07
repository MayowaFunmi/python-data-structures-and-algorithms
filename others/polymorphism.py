class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")
        
    def add(self, x, y):
        print(x + y)

class Penguin:

    def fly(self):
        print("Penguin can't fly")
    
    def swim(self):
        print("Penguin can swim")

# common interface
def flying_test(x):
    x.fly()

#instantiate objects
blu = Parrot()
peggy = Penguin()
sum = Parrot()
sum.add(7,9)

# passing the object
flying_test(blu)
flying_test(peggy)