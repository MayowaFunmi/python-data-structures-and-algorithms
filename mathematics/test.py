from sympy import symbols
c = symbols('b')
d = symbols('y')
a, b = symbols('g n')

print(b)
print(c)

# expressions
x, y = symbols('x y')
expr = 2*x + y
print(expr)
print(expr.subs(x, 3))  # when x = 3
print(expr.subs(y, -4))
print(expr)
expr3 = expr.subs(x, -4).subs(y, 3)
print(expr3)

# make the expression permanent
expr2 = expr.subs(x, -3)
print(expr2)
print(expr)