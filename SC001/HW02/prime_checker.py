"""
File: prime_checker.py
Name: Chance
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT n1umber.
"""

EXIT = -100


def main():
	"""
	Give me a positive number(>1), ana check whether it is prime number
	Exit if input -100
	"""
	print('Welcome to the prime check!')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		i = 1
		while True:
			if n == 1:
				print(str(n) + ' is not a prime number')
				break
			if n == 2 or n == 3:
				print(str(n) + ' is a prime number')
				break
			while True:
				i += 1
				if n % i == 0:
					print(str(n)+' is not a prime number')
					break
				elif i < n/2:
					print(str(n) + ' is a prime number')
					break
			break


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
