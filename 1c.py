#coding=utf-8
from matplotlib import pyplot
from sympy import exp
K=range(150,251)
p=range(150,251)
for k in range(150,251):
	p[k-150]=0.9394*exp(-3)*K[k-150]-200*0.0018

pyplot.plot(K,p)
pyplot.xlabel('K')
pyplot.ylabel('put price')
pyplot.title('put price & K')
pyplot.show()

