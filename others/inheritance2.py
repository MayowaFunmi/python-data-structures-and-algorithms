class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
    def sumOfAngles(self):
            sum = ((2*self.n - 4) *90)
            print("The sum of angles = ", sum)
            
            
class Triangle(Polygon):
    def __init__(self):
        #Polygon.__init__(self, 3)
        super().__init__(3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is :', area)
        
        
class Quadrilateral(Polygon):
        def __init__(self):
            super().__init__(4)
        
t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()
t.sumOfAngles()
q = Quadrilateral()
q.sumOfAngles()