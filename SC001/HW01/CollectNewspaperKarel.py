"""
File: CollectNewspaperKarel.py
Name: Chance
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is at (3,4) and facing east
    post-condition: Karel is at (3,4), facing east
    """
    move_to_newspaper()
    take_newspaper_to_home()


def move_to_newspaper():
    """
    pre-condition: Karel is at (3,4) and facing east
    post-condition: Karel is at (6,3), facing east
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def take_newspaper_to_home():
    """
    pre-condition: Karel is at (6,3), facing east
    post-condition: Karel is at (3,4), facing east
    """
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
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
