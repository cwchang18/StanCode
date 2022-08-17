"""
File: blur.py
Name: Chance
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image
    :return: SimpleImage, the updated image with blurred
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            new_img_pixel = new_img.get_pixel(x, y)

            # initial Condition
            new_img_pixel_sum_red = 0
            new_img_pixel_sum_green = 0
            new_img_pixel_sum_blue = 0
            new_img_pixel_times = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x+i < img.width:
                        if 0 <= y+j < img.height:
                            pixel = img.get_pixel(x+i, y+j)
                            new_img_pixel_sum_red += pixel.red
                            new_img_pixel_sum_green += pixel.green
                            new_img_pixel_sum_blue += pixel.blue
                            new_img_pixel_times += 1

            # calculate the pixel.red/green/blue
            new_img_pixel.red = new_img_pixel_sum_red // new_img_pixel_times
            new_img_pixel.green = new_img_pixel_sum_green // new_img_pixel_times
            new_img_pixel.blue = new_img_pixel_sum_blue // new_img_pixel_times
    return new_img


def main():
    """
    (1) give the blurred operation times
    (2) blur the picture many times
    (3) show the blurred picture
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
