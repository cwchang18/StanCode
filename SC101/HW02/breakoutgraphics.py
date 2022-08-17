"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15     # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5       # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(2*ball_radius, 2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, x=(window_width-2*ball_radius)/2, y=(window_height-2*ball_radius)/2)

        # Default initial velocity for the ball
        self.__vx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__vx = -self.__vx
        self.__vy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmousemoved(self.move)
        onmouseclicked(self.click)

        # Draw bricks
        for i in range(brick_rows):
            if i//2 % 5 == 0:
                color = 'red'
            elif i//2 % 5 == 1:
                color = 'orange'
            elif i//2 % 5 == 2:
                color = 'yellow'
            elif i//2 % 5 == 3:
                color = 'green'
            else:
                color = 'blue'
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=j*(brick_width+brick_spacing),
                                y=i*(brick_height+brick_spacing)+brick_offset)

        self.paddle_offset = paddle_offset
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height

        self.mode = ''

        self.energy = 0
        self.skill_num = 0
        self.is_on_skill = 0
        self.change_color = 0

        self.mouse_x = 0
        self.mouse_y = 0

        self.brick_remove = 0
        self.brick_total = brick_cols * brick_rows

    def move(self, mouse):
        if mouse.x - self.paddle.width/2 < 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width/2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def click(self, mouse):
        self.mouse_x = mouse.x
        self.mouse_y = mouse.y
        if self.mode == 'IDLE':
            self.mode = 'PLAY'
        if self.mode == 'PLAY' and self.is_on_skill > 0:
            self.mode = 'SKILL'

    def set_mode(self, mode):
        self.mode = mode

    def get_mode(self):
        return self.mode

    def set_skill(self, skill_num, energy):
        self.energy = energy
        self.skill_num = skill_num
        if energy > 100 and skill_num > 0:
            self.is_on_skill = 1

    def play_mode(self):
        self.ball.move(self.__vx, self.__vy)

        # y rebound
        maybe_object = self.window.get_object_at(self.ball.x+self.ball.width/2.01, self.ball.y+self.ball.height)
        if maybe_object is None:
            maybe_object = self.window.get_object_at(self.ball.x+self.ball.width/2.01, self.ball.y)
        if maybe_object is not None:
            if maybe_object is self.paddle:
                # vy force up
                if self.__vy > 0:
                    self.__vy *= -1
            else:
                # not paddle -> brick remove
                self.window.remove(maybe_object)
                self.brick_remove += 1
                self.__vy *= -1
        # Up Condition (Force Down)
        if self.ball.y < 0:
            if self.__vy < 0:
                self.__vy *= -1

        # x rebound
        maybe_object = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height/2.01)
        if maybe_object is None:
            maybe_object = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height/2.01)
        if maybe_object is not None:
            if maybe_object is not self.paddle:
                # not paddle -> brick remove
                self.window.remove(maybe_object)
                self.brick_remove += 1
                self.__vx *= -1
        # Left/Right Condition (Force Right/LEFT)
        if self.ball.x < 0:
            if self.__vx < 0:
                self.__vx *= -1
        elif self.ball.x + self.ball.width > self.window.width:
            if self.__vx > 0:
                self.__vx *= -1

        # loss one heart (Down Condition)
        if self.ball.y > self.window.height:
            self.mode = 'IDLE'
            self.ball.x = (self.window.width-self.ball.width)/2
            self.ball.y = (self.window.height-self.ball.height)/2

        # Over the game
        if self.brick_remove == self.brick_total:
            self.mode = 'PASS'

    # 2x paddle
    def skill(self):
        self.window.remove(self.paddle)
        self.paddle_width *= 2
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = 'black'
        self.paddle.color = 'black'
        self.window.add(self.paddle, x=self.mouse_x - self.paddle_width/2, y=self.window.height-self.paddle_offset)
        self.is_on_skill = 0
        self.change_color = 0
        self.mode = 'PLAY'

    # already 2x paddle
    def on_skill(self):
        if self.is_on_skill == 1 and self.change_color == 0:
            self.window.remove(self.paddle)
            self.paddle = GRect(self.paddle_width, self.paddle_height)
            self.paddle.filled = True
            self.paddle.fill_color = 'red'
            self.paddle.color = 'red'
            self.window.add(self.paddle, x=self.mouse_x - self.paddle_width/2, y=self.window.height-self.paddle_offset)
            self.change_color = 1
