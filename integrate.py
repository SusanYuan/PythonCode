#coding=utf-8
from sympy import integrate, exp
from sympy.abc import x, y
def f(x):
	return float('%.10f' %integrate(exp(-0.5*y*y)/sqrt(2*pi),(y,x,0)))

def df(x):
	return -exp(-0.5*x*x)/sqrt(2*pi)

def g(x):
	return x+(0.5-f(x))/df(x)

x=0
r=1

while x>-15:
	x1=g(x)
	r=abs(f(x1)-0.5)
	if r<1e-4:
		break
	x=x1

print f(x1)

