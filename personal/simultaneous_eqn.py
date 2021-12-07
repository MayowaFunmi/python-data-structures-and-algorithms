# INPUT    THE    COEFFICIENT    OF    EQN    1
print("Equation 1.....")
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))

#INPUT THE COEFFICIENTS OF EQUATION 2
print("Equation 2....")
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))

print(a1,"x + ", b1,"y = ", c1,"---- eqn 1")
print(a2,"x + ", b2,"y = ", c2,"----- eqn 2")

#USING CRAMER’S RULE…
D = (a1 * b2) - (a2 * b1)
Dx = (c1 * b2) - (c2 * b1)
Dy = (a1 * c2) - (a2 * c1)
x = Dx/D
y = Dy/D

#DISPLAY THE  RESULTS
print("x = ", x)
print("y = ", y)