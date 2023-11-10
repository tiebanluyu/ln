import sympy as sy
x=sy.symbols("x")
fx=sy.ln(x)+2*x-6
r=sy.solve(fx,x)
r=r[0]#因为一个方程可能有多个解，所以这里返回的是list
print(str(r.n(100)))