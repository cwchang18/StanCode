"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10        # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():

    # call
    graphics = BreakoutGraphics()

    # Variation Define
    num_lives = NUM_LIVES
    mode = 'IDLE'
    graphics.set_mode(mode)
    # loss heart check
    on_game = 0
    # skill define
    energy = 0
    skill_num = 3

    # Add the animation loop here!
    while num_lives > 0:
        if skill_num == 0:
            energy = -1
        elif skill_num > 0 and energy < 100 and mode == 'PLAY':
            energy += 0.1

        # get mode
        mode = graphics.get_mode()
        # set skill
        graphics.set_skill(skill_num, energy)
        # is on skill?
        graphics.on_skill()

        # IDLE mode
        if mode == 'IDLE':
            if on_game == 1:
                on_game = 0
                num_lives -= 1
            pause(FRAME_RATE)

        # PLAY mode
        elif mode == 'PLAY':
            on_game = 1
            graphics.play_mode()
            pause(FRAME_RATE)

        # SKILL mode
        elif mode == 'SKILL':
            energy = 0
            skill_num -= 1
            graphics.skill()

        # PASS mode
        elif mode == 'PASS':
            break

    # END Condition
    if mode == 'PASS':
        print('You win')
    else:
        print('You loss')


if __name__ == '__main__':
    main()
