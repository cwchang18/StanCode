"""
File: extension4_narcissistic_checker.py
Name: Chance
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""


EXIT = -100


def main():
    """
    Check this input number is narcissistic number or not
    Exit if input -100
    """
    print('Welcome to the narcissistic checker!')
    while True:
        num = int(input('n: '))
        if num == EXIT:
            print('Have a good one!')
            break
        power = 0
        exit_temp = 0
        sum_rem_power = 1
        while True:
            # Special Case all 0/1 numbers
            if exit_temp == sum_rem_power:
                print(str(num) + ' is not a narcissistic number')
                break
            exit_temp = sum_rem_power
            power += 1
            sum_rem_power = 0
            num_temp = num
            while True:
                sum_rem_power = sum_rem_power + (num_temp % 10)**power
                num_temp = int(num_temp/10)
                # for debug
                # print(num_temp)
                # print(sum_rem_power)
                if num_temp == 0:
                    break
            if sum_rem_power > num:
                print(str(num) + ' is not a narcissistic number')
                break
            elif sum_rem_power == num:
                print(str(num) + ' is a narcissistic number')
                break


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    main()
