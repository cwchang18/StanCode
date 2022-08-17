"""
File: hailstone.py
Name: Chance
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    Give me a positive number
    If number is odd -> n = 3n+1
    If number is even -> n = n/2
    Routing work and final n = 1
    list all operation
    """
    print('This program computes Hailstone sequence.')
    print('')
    number = int(input('Enter a number: '))
    times = 0
    while True:
        # Final n = 1
        if number == 1:
            break
        # Even
        elif number % 2 == 0:
            print(str(int(number)) + ' is even, so I take half: ' + str(int(number/2)))
            number = number / 2
        # odd
        else:
            print(str(int(number)) + ' is odd, so I take 3n+1: ' + str(int(number * 3 + 1)))
            number = number * 3 + 1
        times += 1
    if number == 1:
        print('It took '+str(times)+' steps to reach 1')
    else:
        print('This is not positive number')

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
    main()
