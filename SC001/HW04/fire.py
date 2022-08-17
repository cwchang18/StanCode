"""
File: fire.py
Name: Chance
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, the updated image with highlight fire and gray background
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue)//3
        if pixel.red > HURDLE_FACTOR * avg:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return img


def main():
    """
    (1) show origin picture
    (2) highlight the fire (pixel: red > 1.05x avg -> red; others -> gray)
    (3) show highlight picture
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
