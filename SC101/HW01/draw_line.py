"""
File: draw_line
Name: Chance
-------------------------
Two position from two clicks form a line
First click form a reference point
Two click form a line and remove the ref. point
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()

# Global Variation
SIZE = 10
click_on_work = 0
x = 0
y = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(mouse):
    global click_on_work, x, y

    # First click
    if click_on_work == 0:
        click_on_work = 1
        click_circle = GOval(SIZE, SIZE)
        click_circle.color = 'red'
        x = mouse.x
        y = mouse.y
        window.add(click_circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)

    # Second click
    else:
        click_on_work = 0
        window.remove(window.get_object_at(x=x, y=y))
        line = GLine(x, y, mouse.x, mouse.y)
        window.add(line)


if __name__ == "__main__":
    main()
