"""
File: name_sq.py (extension)
Name: Chance
----------------------------
This program is an extension of assignment3!
It will ask the user to provide a name, 
and the square pattern of the given name 
will be printed on the console.
"""


def main():
    """
    Give a string.
    print the square words
    and read
    (1) from left top to right top
    (2) from left top to left bottom
    (3) from right bottom to right top
    (4) from right bottom to left bottom
    """
    print('This program prints a name in a square pattern!')
    name = input('Name:')
    # First Row
    print(name)
    num_name = len(name)
    # Second to num_name-1 Row
    for i in range(num_name-2):
        ans = ''
        ans += name[i+1]
        for j in range(num_name-2):
            ans += ' '
        ans += name[num_name-2-i]
        print(ans)
    # Final Row (Reverse word)
    for i in range(num_name):
        print(name[num_name-1-i], end='')
    print('')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
