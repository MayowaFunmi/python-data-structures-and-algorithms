from sympy import symbols, exp

# quadratic expressions
x, y, z = symbols('x y z')
expr = y + 2*x**2 + z**(-3)
print(expr)

expr2 = expr.subs(y, 2*x)
print(expr2)

# more expressions
n, Q, R, T = symbols('n, Q, R, T')
expr = n*exp(-Q/(R*T))
print(expr)
total = expr.subs(n, 3.48e-6).subs(Q, 12700).subs(R, 8031).subs(T, 1000+273)
print(total)
print(total.evalf())
print(total.evalf(4))