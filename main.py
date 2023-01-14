import pgzrun
import random

from pgzero import screen
from pgzero.actor import Actor
from pgzero.constants import mouse
from pgzero.keyboard import keyboard

TITLE = "Christmas Breakout"
WIDTH = 600
HEIGHT = 600

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

ball_x_speed = -1
ball_y_speed = -1

paddle.x = 120
paddle.y = 420


def draw():
    paddle.draw()
    ball.draw()


# ball physics

def update():
    global ball_x_speed, ball_y_speed
    if keyboard.left:
        paddle.x = paddle.x - 5
    if keyboard.right:
        paddle.x = paddle.x + 5


if paddle.colliderect(ball):
    ball_y_speed *= -1
    # randomly move ball left or right on hit
    rand = random.randint(0, 1)
    if rand:
        ball_x_speed *= -1


def update_ball():
    global ball_x_speed, ball_y_speed
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1


def on_mouse_move(pos):
    x, y = pos
    paddle.x = x


pgzrun.go()
