from math import *

x = 0
a = 0
b = 0

def fist_form(a,x):
	return (atan(sqrt(abs(x))) + pow(x,2)) / (log(2*x) + pow(e, abs(-x-5))) + 3*a - 0.2

def second_form(a,b,x):
	return pow(sin(6*a),2) + 8 * tan(pow(b,3)) - 5/(a*b*x) * pow(3.82,a)

print(second_form(2,14,2))