"""
File: mirror_lake.py
Name: Chance
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image (with respect to current directory)
    :return: SimpleImage, the updated image with 2x img.height and reflect
    """
    img = SimpleImage(filename)
    b_img = SimpleImage.blank(img.width, 2 * img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            b1_pixel = b_img.get_pixel(x, y)
            b1_pixel.red = pixel.red
            b1_pixel.green = pixel.green
            b1_pixel.blue = pixel.blue
            b2_pixel = b_img.get_pixel(x, 2 * img.height - y - 1)
            b2_pixel.red = pixel.red
            b2_pixel.green = pixel.green
            b2_pixel.blue = pixel.blue
    return b_img


def main():
    """
    (1) show origin picture
    (2) reflect the picture in y-dir.
    (3) show reflected picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
