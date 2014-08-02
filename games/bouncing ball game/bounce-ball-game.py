# A Bouncing Ball Game
# Author: Victa Li
# Date: July, 2014
from tkinter import *
import time
import random


SLEEP_TIME = 0.01
PADDLE_SPEED = [20, 10]
BALL_SPEED = [1, 3]
# Model for the Ball class
# canvas is the tkinter current canvas
# color is the color of the ball
# paddle_pos is the current position of the paddle
# speed [x, y] is the absolute speed of the ball
class Ball:
    def __init__(self, canvas, color, speed):
        self.canvas = canvas
        self.color = color
        self.ball = canvas.create_oval(0, 0, 10, 10, fill=color)
        self.speed = speed
        canvas.move(self.ball, 250, 250)

    # paddle is the identifier of the paddle element
    # (0,1)---------
    #   |          |
    #   |          |
    #   ---------(3,4)
    def move(self, paddle):
        cur_pos = self.canvas.coords(self.ball)
        paddle_pos = self.canvas.coords(paddle)
        self.canvas.move(self.ball, self.speed[0], self.speed[1])
        if cur_pos[1] <= 0:
            self.speed[1] = abs(self.speed[1])
        if cur_pos[3] >= self.canvas.winfo_height():
            self.speed[1] = -abs(self.speed[1])
        if cur_pos[0] <= 0:
            self.speed[0] = abs(self.speed[0])
        if cur_pos[2] >= self.canvas.winfo_width():
            self.speed[0] = -abs(self.speed[0])
        # check against the top surface of the paddle
        if cur_pos[2] >= paddle_pos[0] and cur_pos[2] <= paddle_pos[2] and cur_pos[3] >= paddle_pos[1] and cur_pos[3] <= paddle_pos[3] and self.speed[1] > 0:
            self.speed[1] = -abs(self.speed[1])
        if cur_pos[0] >= paddle_pos[0] and cur_pos[0] <= paddle_pos[2] and cur_pos[3] >= paddle_pos[1] and cur_pos[3] <= paddle_pos[3] and self.speed[1] > 0:
            self.speed[1] = -abs(self.speed[1])
        # check against the bottom surface of the paddle
        if cur_pos[2] >= paddle_pos[0] and cur_pos[2] <= paddle_pos[2] and cur_pos[1] <= paddle_pos[3] and cur_pos[1] >= paddle_pos[1] and self.speed[1] < 0:
            self.speed[1] = abs(self.speed[1])
        if cur_pos[0] >= paddle_pos[0] and cur_pos[0] <= paddle_pos[2] and cur_pos[1] <= paddle_pos[3] and cur_pos[1] >= paddle_pos[1] and self.speed[1] < 0:
            self.speed[1] = abs(self.speed[1])


class Paddle:
    def __init__(self, canvas, color, x_speed, y_speed):
        self.canvas = canvas
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.paddle = self.canvas.create_rectangle(0, 0, 60, 10, fill=color)
        canvas.move(self.paddle, 250, 400)
        self.canvas.bind_all('<KeyPress>', self.move)

    def move(self, event):
        cur_pos = self.canvas.coords(self.paddle)
        x_speed = self.x_speed
        y_speed = self.y_speed
        if event.keysym == 'Left':
            x_speed = -(abs(self.x_speed))
            y_speed = 0
            if cur_pos[0] <= 0:
                x_speed = 0
        if event.keysym == 'Right':
            x_speed = abs(self.x_speed)
            y_speed = 0
            if cur_pos[2] >= self.canvas.winfo_width():
                x_speed = 0
        if event.keysym == 'Up':
            x_speed = 0
            y_speed = -(abs(self.y_speed))
            if cur_pos[1] <= 0:
                y_speed = 0
        if event.keysym == 'Down':
            x_speed = 0
            y_speed = abs(self.y_speed)
            if cur_pos[3] >= self.canvas.winfo_height():
                y_speed = 0
        self.canvas.move(self.paddle, x_speed, y_speed)

class HitBlock:
	# x and y are the coordinates of the top-left corner of the hitblock
	def __init__(self, canvas, color, x, y):
		self.canvas = canvas
		self.color = color
		self.x = x
		self.y = y
		self.hit_block = self.canvas.create_rectangle(self.x, self.y, self.x+20, self.y+20, fill=self.color)
		canvas.move(self.hit_block, self.x, self.y)
    
# Setup the tk environment: title and configuration
def setup(tk):
    tk.title("Bounce Ball Game")
    tk.resizable(0,0)
    tk.wm_attributes("-topmost", 0)


# Create hitblock(s) at random locations
def create_hit_blocks(canvas, num_blocks):
	hit_blocks = []
	i = 0
	while i < num_blocks:
		x = random.randint(100, 200)
		y = random.randint(100, 200)
		hit_blocks.append(HitBlock(canvas, "white", x, y))
		i = i + 1
	return hit_blocks

# Main function

# setup the tkinter
tk = Tk()
setup(tk)

# setup the canvas and initaite the elements
canvas = Canvas(tk, width=500, height=500, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
paddle = Paddle(canvas=canvas, color="blue", x_speed=PADDLE_SPEED[0], y_speed=PADDLE_SPEED[1])
ball = Ball(canvas=canvas, color="red", speed=BALL_SPEED)
hit_blocks = create_hit_blocks(canvas, 3)

# main loop
while True:
    tk.update()
    ball.move(paddle.paddle)
    tk.update()
    time.sleep(SLEEP_TIME)
    
    
