"""
File: bouncing_ball
Name: Chance
-------------------------
Give some balls information to simulate the ball trace
Times/VX/DELAY/GRAVITY/SIZE/REDUCE/START_X,y
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

TIMES = 3
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# Global Variable
window = GWindow(800, 500, title='bouncing_ball.py')
bounce = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    # Global Variable
    global bounce

    # initial variable
    below_ground = 0

    # add ball
    ball_drag = GOval(SIZE, SIZE)
    ball_drag.filled = True
    ball_drag.fill_color = 'black'

    # click
    onmouseclicked(click)

    for i in range(TIMES):
        # initial ball condition
        vy = 0
        window.add(ball_drag, x=START_X, y=START_Y)

        # wait for click
        while True:
            pause(DELAY)
            if bounce == 1:
                break

        # ball move
        while ball_drag.x < window.width:
            if ball_drag.y + SIZE < window.height:
                vy += GRAVITY
                below_ground = 0
            elif below_ground:
                vy = vy
            else:
                vy = -vy * REDUCE
                below_ground = 1

            ball_drag.x = ball_drag.x + VX
            ball_drag.y = ball_drag.y + vy
            pause(DELAY)

        # Wait for click
        bounce = 0

    # OBOB condition
    window.add(ball_drag, x=START_X, y=START_Y)


def click(_):
    # start
    global bounce
    bounce = 1


if __name__ == "__main__":
    main()
