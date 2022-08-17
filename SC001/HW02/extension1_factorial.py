"""
File: extension1_factioral.py
Name: Chance
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
	"""
	Give me a positive integer, and I will list the answer of factorial
	Exit if input -100
	"""
	print('Welcome to stanCode factorial master!')
	while True:
		int_fact = int(input('Give me a number, and I will list the answer of factorial: '))
		if int_fact == EXIT:
			print('- - - - - See ya! - - - - - -')
			break
		if int_fact < 1:
			print('Please input the positive integer')
		else:
			out_fact = 1
			for i in range(int_fact):
				out_fact = out_fact * (i+1)
			print('Answer: ' + str(out_fact))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()