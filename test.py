import numpy as np

print('Hello World!')



#function for determining the circumference of  a circle
def cir(r):
	"""This function calculates the circumference of a circle
	input r: radius of the circle
	output l: circumference of the circle"""
 
	return 2*np.pi*r
#function for determining the area of a circle
def area(r):
	"""This function calculates the area of a circle
        input r: radius of the circle
        output a: area of the circle"""
	
	return np.pi*r**2



r = float(input("What is the radius of the circle[cm]?:"))

print('The circumference of the circle is %0.2f cm'% cir(r)) 
print('The ara of the circle is %0.2f cm^2' % area(r))
