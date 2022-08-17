"""
File: CheckerboardKarel.py
Name: Chance
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (1,1) and facing east
    Post-condition: Not define. But I want that Karel is at most
                    northeastern position and facing east
    """
    while not facing_north():
        go_go_put()
    go_easternmost()


def go_go_put():
    """
    (1) First put beeper for OBOB
    (2) a. move, move, put
        b. move, turn left(right), move, put, turn left(right)
        c. turn left(right), move, turn left(right), move, put
        d. turn left(right), move, turn left(right),
            turn right(left), move, put, turn right(left)
        e. No activity when front is wall and facing north
    """
    # First for OBOB
    if not on_beeper():
        put_beeper()
    # front is clear
    if front_is_clear():
        move()
        # front front put beeper
        if front_is_clear():
            move()
            put_beeper()
        else:
            if facing_east():
                turn_left()
                # facing east -> right top put beeper, facing west
                if front_is_clear():
                    move()
                    put_beeper()
                    turn_left()
            else:
                turn_right()
                # facing west -> left top put beeper, facing east
                if front_is_clear():
                    move()
                    put_beeper()
                    turn_right()
    # front is wall
    else:
        if facing_east():
            turn_left()
            if front_is_clear():
                move()
                turn_left()
                # facing east -> left top put beeper, facing west
                if front_is_clear():
                    move()
                    put_beeper()
                # top top put beeper
                else:
                    turn_right()
                    if front_is_clear():
                        move()
                        put_beeper()
                        turn_left()
        else:
            turn_right()
            if front_is_clear():
                move()
                turn_right()
                # facing west -> right top put beeper, facing east
                if front_is_clear():
                    move()
                    put_beeper()
                # top top put beeper
                else:
                    turn_left()
                    if front_is_clear():
                        move()
                        put_beeper()
                        turn_left()


def go_easternmost():
    """
    pre-condition: at the northernmost and facing north
    post-condition: on the most northeaster adn facing east
    """
    if not left_is_clear():
        turn_right()
        while front_is_clear():
            move()
    else:
        turn_right()


def turn_right():
    # turn left 3 times #
    turn_left()
    turn_left()
    turn_left()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
