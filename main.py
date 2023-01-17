import pgzrun
import random
from pgzero.actor import Actor
import pygame

WIDTH = 600
HEIGHT = 600
RADIUS = 20
TITLE = "Christmas Breakout"


class Obstacle:
    def __init__(self, x, y, strength, color):
        self.x = x
        self.y = y
        self.strength = strength
        self.color = color

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), RADIUS, self.color)


class Paddle:
    def __init__(self):
        self.actor = Actor("paddleblue.png", center=(WIDTH // 2, HEIGHT - 30))

    def draw(self):
        self.actor.draw()


class Ball:
    def __init__(self, speed: int):
        self.actor = Actor('ballblue.png', center=(WIDTH // 2, HEIGHT // 2))
        self.speed = speed
        self.ball_dx = self.speed
        self.ball_dy = self.speed
        self.radius = 20

    def update(self):
        self.actor.x += self.ball_dx
        self.actor.y += self.ball_dy

    def draw(self):
        self.actor.draw()


paddle = Paddle()
obstacles = []
points = 0
dictionary = {
    1: 'blue', 2: 'green', 3: 'purple'
}
n = 10
m = 9
x = 50
for obstacle in range(n):
    strength = random.randint(1, 3)
    obstacles.append(Obstacle(x, 100, strength, dictionary[strength]))
    x = x + 55

x = 100
for obstacle in range(m):
    strength = random.randint(1, 3)
    obstacles.append(Obstacle(x, 150, strength, dictionary[strength]))
    x = x + 50


def draw():
    screen.clear()

    for obstacle in obstacles:
        obstacle.draw()

    if points == 19:
        screen.draw.text(f"You won the game!", (HEIGHT / 2 - 200, WIDTH / 2), color=(200, 200, 0), fontsize= 50)


def update():
    for obstacle in obstacles:
        if abs(ball.actor.y - obstacle.y) < RADIUS * 2 and abs(ball.actor.x - obstacle.x) < RADIUS * 2:
            ball.ball_dx *= -1
            ball.ball_dy *= -1
            global points
            obstacle.strength -= 1
            if obstacle.strength == 0:
                points += 1
                obstacles.remove(obstacle)


def on_mouse_move(pos):
    x, y = pos
    paddle.actor.x = x


pgzrun.go()
