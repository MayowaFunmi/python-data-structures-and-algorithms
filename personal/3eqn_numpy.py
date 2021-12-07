import numpy as np

print("Coefficients of eqn 1...")
a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))
d1 = int(input("Enter d1: "))

print("Coefficients of eqn 2...")
a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: "))
c2 = int(input("Enter c2: "))
d2 = int(input("Enter d2: "))

print("Coefficients of eqn 3...")
a3 = int(input("Enter a3: "))
b3 = int(input("Enter b3: "))
c3 = int(input("Enter c3: "))
d3 = int(input("Enter d3: "))

print("Solving 3 equations simultaneously...")

A = np.array([[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]])
b = np.array([d1, d2, d3])
x = np.linalg.solve(A, b)
print("x = ", x[0])
print("y = ", x[1])
print("z = ", x[2])