"""
File: extension3_triangular_checker.py
Name: Chance
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""


import math
EXIT = -100


def main():
    """
    Check this input number is triangular number or not
    Exit if input -100
    """
    print('Welcome to the triangular number checker')
    while True:
        num = int(input('n: '))
        if num == EXIT:
            print('Have a good one!')
            break
        square = math.sqrt(num+num)
        int_square = int(square)
        if num == int_square * (int_square+1)/2:
            print(str(num)+' is a triangular number')
        else:
            print(str(num)+' is not a triangular number')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
