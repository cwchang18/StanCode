"""
File: StoneMasonKarel.py
Name: Chance
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1) and facing east
    post-condition: Karel is at most southeastern and facing east
    """
    fix_pillar()
    while front_is_clear():
        go_next_pillar()
        fix_pillar()
    go_far_southeast()


def fix_pillar():
    """
    pre-condition: Karel is at top or bottom, facing east
    post-condition: (1) pre-condition Karel is at top -> post-condition Karel is at bottom, facing east
                    (2) pre-condition Karel is at bottom -> post-condition Karel is at top, facing east
    """
    if left_is_clear():
        turn_left()
    else:
        turn_right()

    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()

    if facing_north():
        turn_right()
    else:
        turn_left()


def go_next_pillar():
    """
    pre-condition: Karel is at (x,y) and facing east
    post-condition: Karel is at (x+4,y) and facing east
    """
    move()
    move()
    move()
    move()


def go_far_southeast():
    """
    pre-condition: Karel is at easternmost, and Karel is at top or bottom of the pillar, and facing east
    post-condition: Karel is at most southeastern and facing east
    """
    if not left_is_clear():
        turn_right()
        while front_is_clear():
            move()
        turn_left()


def turn_right():
    # turn left 3 times #
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
