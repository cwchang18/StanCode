"""
File: extension1_MidpointKarel.py
Name: Chance
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1) and facing east
    post-condition: Karel is at (Mid,1) , Mid(X=4) = 2 or 3, Mid(X=3) = 2
    X+1, Y+2
    """
    if front_is_clear():
        move()
        turn_left()
    while front_is_clear():
        if front_is_clear():
            move()
        if front_is_clear():
            move()
        if front_is_clear():
            turn_right()
            if front_is_clear():
                move()
            turn_left()
    turn_around()
    while front_is_clear():
        move()
    put_beeper()


def turn_right():
    # turn left 3 times #
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    # turn left 2 times #
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
