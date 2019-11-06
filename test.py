import numpy as np

print('Hello World!')



#function for determining the circumference of  a circle
def cir(r):
	"""This function calculates the circumference of a circle
	input r: radius of the circle
	outpyt l: circumference of the circle"""
 
	return 2*np.pi*r

r = float(input("What is the radius of the circle[cm]?:"))

print('The circumference of the circle is %0.2f cm'% cir(r)) 
