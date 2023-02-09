import sympy as sym
import os

#solve equation
# os.system('cls')
# x, y = sym.symbols('x y')
# expr = x + 2*y 
# res = sym.expand(x*expr)
# print(res)
# res = sym.solve(res,x)
# print(res)

#substitution
# os.system('cls')
# a,b = sym.symbols('a b')
# expr = 3*a**3-6*a**2*b+9*a*b**2
# expr = expr/3*a
# expr = expr.subs(a,2)
# print(expr)

#reduction
os.system('cls')
a,b = sym.symbols('a b')
expr = 3*a**3-6*a**2*b+9*a*b**2
expr = sym.expand(expr/(3*a))
print(expr)