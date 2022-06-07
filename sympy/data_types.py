import sympy as sp


# Integer Type
x = sp.Symbol('x')
expr = x**(sp.Integer(1) / sp.Integer(3))
print(expr)