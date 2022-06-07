import sympy as sp

root = sp.sqrt(2)
print(root)
print(root**2)


# symbols
# make a symbol

x = sp.Symbol('x')
print(x)

# a simple expression
print(2* + 5)
print(2*x + x + 5)
print(2*x / 6)

# expand expression
expr = x*(x+2)
print(expr)
print(expr.expand())    # expand as a method
print(sp.expand(expr))  # expand as a functiom


# define multiple symbols at once
y = sp.symbols('s t')
print(y)

s, t = sp.symbols('s, t')

poly = t*(s+2)*(t-3)
print(poly)
print(poly.expand())


# factor expressions
expr = x**2 + 2*x - 15
print(expr)
print(expr.factor())


# define multiple symbols at once
x_v = sp.symbols('x0:5')
print(x_v)