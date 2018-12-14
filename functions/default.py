def exponent(num, power = 2):
	return num ** power

print(exponent(2, 3)) #8
print(exponent(3)) #9
print(exponent(9))

def add(a=10, b=20):
	return a+b

print(add())
print(add(1,10)) #11


"""

Why?

Allows you to be more defensive
Avoids error with incorrect parameters
More readable examples!

Make sure:

default parameters must go at end or
all parameters must be default.

"""

def add(a, b):
	return a+b

def math(a, b, fn = add):
	return fn(a,b)

def sub(a, b):
	return a-b

print(math(2, 4))
print(math(2, 2, sub))
