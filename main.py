import pgzrun
import random

from pgzero import screen
from pgzero.actor import Actor

TITLE = "Christmas Breakout"
WIDTH = 600
HEIGHT = 500

paddle = Actor("paddleblue.png")
paddle.x = 120
paddle.y = 420

ball = Actor("ballblue.png")
ball.x = 30
ball.y = 300

paddle.x = 120
paddle.y = 420


def draw():
    paddle.draw()
    ball.draw()


# ball physics
def update():
    update_ball()


def update_ball():
    ball.x -= 1
    ball.y -= 1


pgzrun.go()
