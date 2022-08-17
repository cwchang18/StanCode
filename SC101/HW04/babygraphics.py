"""
File: babygraphics.py
Name: Chance
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
WORD_TYPE = 'Arial'
WORD_SIZE = 10
RADIUS = 5


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE + year_index * width / len(YEARS)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    # Horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, canvas.winfo_width()-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, canvas.winfo_height()-GRAPH_MARGIN_SIZE,
                       canvas.winfo_width()-GRAPH_MARGIN_SIZE, canvas.winfo_height()-GRAPH_MARGIN_SIZE)

    # Vertical line
    for i in range(len(YEARS)):
        year_line_x = get_x_coordinate(canvas.winfo_width(), i)
        canvas.create_line(year_line_x, 0, year_line_x, canvas.winfo_width())
        canvas.create_text(year_line_x, canvas.winfo_height()-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW,
                           font=(WORD_TYPE, WORD_SIZE))


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    # draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #

    # Initial Variable
    x1 = 0
    y1 = 0

    # lookup name for loop
    for i in range(len(lookup_names)):

        # color select
        if i == 0:
            color = 'red'
        elif i == 1:
            color = 'orange'
        elif i == 2:
            color = 'purple'
        elif i == 3:
            color = 'green'
        elif i == 4:
            color = 'blue'
        else:
            color = 'black'

        # Gen Plot
        for j in range(len(YEARS)):
            year_str = str(YEARS[j])

            # Initial Case
            if j == 0:
                x1 = get_x_coordinate(canvas.winfo_width(), j)

                # name at year -> obtain rank
                if year_str in name_data[lookup_names[i]]:
                    rank1 = int(name_data[lookup_names[i]][year_str])
                    y1 = GRAPH_MARGIN_SIZE + rank1 * ((canvas.winfo_height() - 2*GRAPH_MARGIN_SIZE) / MAX_RANK)
                    canvas.create_text(x1, y1, text=lookup_names[i]+' '+str(rank1), anchor=tkinter.SW, fill=color,
                                       font=(WORD_TYPE, WORD_SIZE))

                # name at year -> no obtain rank (*)
                else:
                    y1 = canvas.winfo_height() - GRAPH_MARGIN_SIZE
                    canvas.create_text(x1, y1, text=lookup_names[i]+' *', anchor=tkinter.SW, fill=color,
                                       font=(WORD_TYPE, WORD_SIZE))

                # gen oval
                canvas.create_oval(x1 - RADIUS, y1 - RADIUS, x1 + RADIUS, y1 + RADIUS, fill=color)

            else:
                x2 = get_x_coordinate(canvas.winfo_width(), j)

                # name at year -> obtain rank
                if year_str in name_data[lookup_names[i]]:
                    rank2 = int(name_data[lookup_names[i]][year_str])
                    y2 = GRAPH_MARGIN_SIZE + rank2 * ((canvas.winfo_height() - 2*GRAPH_MARGIN_SIZE) / MAX_RANK)
                    canvas.create_text(x2, y2, text=lookup_names[i]+' '+str(rank2), anchor=tkinter.SW, fill=color,
                                       font=(WORD_TYPE, WORD_SIZE))
                # name at year -> no obtain rank (*)
                else:
                    y2 = canvas.winfo_height() - GRAPH_MARGIN_SIZE
                    canvas.create_text(x2, y2, text=lookup_names[i]+' *', anchor=tkinter.SW, fill=color,
                                       font=(WORD_TYPE, WORD_SIZE))

                # gen line/oval
                canvas.create_oval(x2 - RADIUS, y2 - RADIUS, x2 + RADIUS, y2 + RADIUS, fill=color)
                canvas.create_line(x1, y1, x2, y2, fill=color, width=3)
                x1 = x2
                y1 = y2


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # test
    # draw_names(canvas, name_data, ['Kylie', 'Nicholas', 'Sonja', 'Lucy', 'Jennifer', 'Wade'])

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
