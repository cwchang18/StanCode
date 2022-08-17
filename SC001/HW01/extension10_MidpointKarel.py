"""
File: extension4_MidpointKarel.py
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
    check most southeastern position
    """
    put_beeper()
    while front_is_clear():
        move_origin()
        while on_beeper():
            if front_is_clear():
                move()
            turn_left()
            if front_is_clear():
                move()
            turn_right()
        put_beeper()
        turn_right()
        while front_is_clear():
            move()
            turn_left()
            if front_is_clear():
                move()
            turn_right()
        if left_is_clear():
            move_origin()
    move_origin()
    while on_beeper():
        pick_beeper()
        if front_is_clear():
            move()
        turn_left()
        if front_is_clear():
            move()
        turn_right()
    turn_right()
    if front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
    facing_south()
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


def facing_south():
    # facing south
    if facing_east():
        turn_left()
    if facing_west():
        turn_right()
    if facing_north():
        turn_around()


def move_origin():
    # move to origin (1,1) and facing east
    facing_south()
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around()


def pick1_world():
    # All position pickup 1 beeper
    while front_is_clear():
        if on_beeper():
            pick_beeper()
        move()
        if not front_is_clear():
            if facing_west():
                turn_right()
                if on_beeper():
                    pick_beeper()
                if front_is_clear():
                    move()
                    turn_right()
            else:
                turn_left()
                if on_beeper():
                    pick_beeper()
                if front_is_clear():
                    move()
                    turn_left()


def stop_y1_beeper():
    # stop Y=1 beeper
    while not on_beeper():
        move()


def change_1_beeper():
    # Post-Condition: The position includes only one beeper
    while on_beeper():
        pick_beeper()
    put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
