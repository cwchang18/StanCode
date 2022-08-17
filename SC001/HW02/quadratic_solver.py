"""
File: quadratic_solver.py
Name: Chance
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	To solve the Unary quadratic equation
	a, b, c all integer
	List the root(s)
	"""
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	if b * b > 4 * a * c:
		x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
		x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
		print('Two roots: '+str(x1)+' , '+str(x2))
	elif b * b == 4 * a * c:
		x = -b / (2 * a)
		print('One root: '+str(x))
	else:
		print('No real roots')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
