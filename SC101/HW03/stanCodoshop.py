"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return ((pixel.red-red)**2+(pixel.green-green)**2+(pixel.blue-blue)**2)**(1/2)


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    # Initial value
    pixel_red_sum = 0
    pixel_green_sum = 0
    pixel_blue_sum = 0
    count = 0

    # sum
    for pixel in pixels:
        pixel_red_sum += pixel.red
        pixel_green_sum += pixel.green
        pixel_blue_sum += pixel.blue
        count += 1

    # return
    return [pixel_red_sum//count, pixel_green_sum//count, pixel_blue_sum//count]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # initial variable
    lst = get_average(pixels)
    best_pixel = pixels[0]
    min_dist = get_pixel_dist(pixels[0], lst[0], lst[1], lst[2])

    # find best pixel
    for pixel in pixels:
        pixel_dist = get_pixel_dist(pixel, lst[0], lst[1], lst[2])
        if pixel_dist < min_dist:
            min_dist = pixel_dist
            best_pixel = pixel

    # return
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for i in range(width):
        for j in range(height):
            pixels = []
            for img in images:
                pixels.append(img.get_pixel(i, j))
            best_pixel = get_best_pixel(pixels)
            result.set_pixel(i, j, best_pixel)
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
