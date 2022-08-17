"""
File: extension2_number_checker.py
Name: Chance
------------------------
This program asks our user for input and checks if the input is a
perfect number、deficient number or an abundant number.

A number is said to be perfect if it is equal to the sum of all its
factors (for obvious reasons the list of factors being considered does
not include the number itself).

A number is considered to be abundant if the sum of its factors
(aside from the number) is greater than the number itself.

And a number is said to be deficient if it is bigger than the sum of all its
factors(aside from the number itself).

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
    """
    Check this integer is perfect, abundant or deficient number
    Exit if input -100
    """
    print('Welcome to the number checker')
    while True:
        num = int(input('n: '))
        if num == EXIT:
            print('Have a good one!')
            break
        sum_fact = 0
        for i in range(num):
            if num % (i+1) == 0:
                sum_fact += (i+1)
        # print('sum_fact' + str(sum_fact))
        if sum_fact - num > num:
            print(str(num) + ' is a abundant number')
        elif sum_fact - num == num:
            print(str(num) + ' is a perfect number')
        else:
            print(str(num) + ' is a deficient number')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
