import pgzrun
import random

from pgzero.actor import Actor
import pygame

WIDTH = 600
HEIGHT = 600
TITLE = "Christmas Breakout"


class Paddle:
    def __init__(self):
        self.actor = Actor("paddle.png", center=(WIDTH // 2, HEIGHT - 30))

    def update(self, ball):
        if self.actor.colliderect(ball.actor):
            ball.ball_dy *= -1
            ball.ball_dx *= 1 if random.randint(0, 1) else -1

    def draw(self):
        self.actor.draw()


class Ball:
    def __init__(self, speed: int):
        self.actor = Actor('ball.png', center=(WIDTH // 2, HEIGHT // 2))
        self.speed = speed
        self.ball_dx = self.speed
        self.ball_dy = self.speed
        self.radius = 13

    def update(self):
        self.actor.x += self.ball_dx
        self.actor.y += self.ball_dy

        if not (0 <= ball.actor.x <= WIDTH):
            self.ball_dx *= -1

        if not (0 <= ball.actor.y <= HEIGHT):
            self.ball_dy *= -1

    def draw(self):
        self.actor.draw()


class Platform:
    pass


paddle = Paddle()
ball = Ball(5)
platform = Platform()


def draw():
    screen.clear()
    paddle.draw()
    ball.draw()


def update(dt):
    ball.update()
    paddle.update(ball)


def on_mouse_move(pos):
    screen.clear()
    x, y = pos
    paddle.actor.x = x


pgzrun.go()
