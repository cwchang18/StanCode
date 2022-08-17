"""
File: best_photoshop_award.py
Name: Chance
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


THRESHOLD1 = 1.01
THRESHOLD2 = 1.2
# Bomb1
POS2X = 0.1
POS2Y = 0.13
SCALE2 = 2.2
# Bomb2
POS3X = 0.4
POS3Y = 0.13
SCALE3 = 2.2
# Bomb3
POS4X = 0.17
POS4Y = 0.22
SCALE4 = 2
# Bomb4
POS5X = 0.33
POS5Y = 0.32
SCALE5 = 1.8
# Bomb5
POS6X = 0
POS6Y = 0.37
SCALE6 = 1.8


def main():
    """
    創作理念：
    (1) 在綠色窗邊想到要寫stanCode的作業與考試
                                    (生氣面目猙獰)
    (2) 想到Jerry是Stanford的學生，傳送到Stanford並開啟血陣
                                    (眼睛也有血絲，牙齒也變黑色)
    (3) 頓時，降落五個砲彈摧毀Stanford大學
                                    (其實很久)
    """
    fig = SimpleImage('image_contest/Chance.png')
    fig.show()
    bg = SimpleImage('image_contest/Chance_bg.png')
    bg.make_as_big_as(fig)
    new_img = combine1(fig, bg)
    new_img.show()
    # Bomb1
    bg2 = bomb(fig, POS2X, POS2Y, SCALE2)
    new_img2 = combine2(new_img, bg2)
    new_img2.show()
    # Bomb2
    bg3 = bomb(fig, POS3X, POS3Y, SCALE3)
    new_img3 = combine2(new_img2, bg3)
    new_img3.show()
    # Bomb3
    bg4 = bomb(fig, POS4X, POS4Y, SCALE4)
    new_img4 = combine2(new_img3, bg4)
    new_img4.show()
    # Bomb4
    bg5 = bomb(fig, POS5X, POS5Y, SCALE5)
    new_img5 = combine2(new_img4, bg5)
    new_img5.show()
    # Bomb25
    bg6 = bomb(fig, POS6X, POS6Y, SCALE6)
    new_img6 = combine2(new_img5, bg6)
    new_img6.show()


def combine1(fig, bg):
    """
    :param fig: SimpleImage, the original image
    :param bg: SimpleImage, the original background
    :return: SimpleImage, the knockout image with new background
    """
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue)/3
            if fig_pixel.green > avg * THRESHOLD1:
                # Green Screen
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


def combine2(fig, bg):
    """
    :param fig: SimpleImage, the original image
    :param bg: SimpleImage, the original background
    :return: SimpleImage, the image with knockout background
    """
    for x in range(bg.width):
        for y in range(bg.height):
            bg_pixel = bg.get_pixel(x, y)
            avg = (bg_pixel.red + bg_pixel.green + bg_pixel.blue)/3
            if bg_pixel.green < avg * THRESHOLD2:
                # Green Screen
                fig_pixel = fig.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return fig


def bomb(fig, pos_x, pos_y, scale):
    """
    :param fig: SimpleImage, the original image
    :param pos_x: float, specified X location - pos_x * fig.width
    :param pos_y: float, specified Y location - pos_y * fig.height
    :param scale: float, bomb scale
    :return: SimpleImage, scaling bomb and specified location
    """
    bomb_img = SimpleImage('image_contest/Chance_bg2.jpg')
    bomb_img.make_as_big_as(fig)
    bomb_img2 = SimpleImage.blank(int(fig.width // scale), int(fig.height // scale))
    for x in range(int(fig.width // scale)):
        for y in range(int(fig.height // scale)):
            bomb_pixel = bomb_img.get_pixel(int(scale * x), int(scale * y))
            bomb2_pixel = bomb_img2.get_pixel(x, y)
            bomb2_pixel.red = bomb_pixel.red
            bomb2_pixel.green = bomb_pixel.green
            bomb2_pixel.blue = bomb_pixel.blue
    bomb_img3 = SimpleImage.blank(fig.width, fig.height)
    for x in range(fig.width):
        for y in range(fig.height):
            if int(pos_x * fig.width) < x < int((pos_x + 1/scale) * fig.width) and \
                    int(pos_y * fig.height) < y < int((pos_y + 1/scale) * fig.height):
                bomb3_pixel = bomb_img3.get_pixel(x, y)
                bomb2_pixel = bomb_img2.get_pixel(x - int(pos_x * fig.width) - 1, y - int(pos_y * fig.height) - 1)
                bomb3_pixel.red = bomb2_pixel.red
                bomb3_pixel.green = bomb2_pixel.green
                bomb3_pixel.blue = bomb2_pixel.blue
            else:
                bomb3_pixel = bomb_img3.get_pixel(x, y)
                bomb3_pixel.red = 0
                bomb3_pixel.green = 255
                bomb3_pixel.blue = 0
    return bomb_img3


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
