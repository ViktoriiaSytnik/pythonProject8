import pgzrun
import random

from pgzero.actor import Actor
import pygame

WIDTH = 600
HEIGHT = 600
radius = 20


class Paddle:

    def __init__(self):
        self.actor = Actor('paddle.png', center=(WIDTH // 2, HEIGHT - 30))

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
        self.radius = 20

    def update(self):
        self.actor.x += self.ball_dx
        self.actor.y += self.ball_dy

        if not (0 <= ball.actor.x <= WIDTH):
            self.ball_dx *= -1

        if not (0 <= ball.actor.y <= HEIGHT):
            self.ball_dy *= -1

    def draw(self):
        self.actor.draw()


class Heart:
    def __init__(self, i, y):
        self.x = 20 + 35 * i
        self.y = y
        self.actor = Actor('heart-3.png', center=(self.x, self.y))

    def draw(self):
        self.actor.draw()


class Obstacle:
    def __init__(self, x, y, strength, colour='purple'):
        self.x = x
        self.y = y
        self.pos = x, y
        self.strength = strength
        self.colour = colour

    def draw(self):
        screen.draw.filled_circle(self.pos, radius, self.colour)


paddle = Paddle()
ball = Ball(5)
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

hearts = []
for i in range(3):
    hearts.append(Heart(i, 20))


def draw():
    screen.clear()
    paddle.draw()
    ball.draw()
    for heart in hearts:
        heart.draw()

    for obstacle in obstacles:
        obstacle.draw()

    screen.draw.text(f"points: {points}", (500, 20), color=(200, 200, 200))

    if points == 19:
        screen.draw.text(f"You won the game!", (HEIGHT / 2 - 200, WIDTH / 2), color=(200, 200, 0), fontsize=50)

    for heart in hearts:
        heart.draw()

    if len(hearts) == 0:
        screen.draw.text(f"You lost the game!", (HEIGHT / 2 - 200, WIDTH / 2), color=(200, 200, 0), fontsize=50)


def update(dt):
    ball.update()
    paddle.update(ball)
    for obstacle in obstacles:
        if abs(ball.actor.y - obstacle.y) < radius * 2 and abs(ball.actor.x - obstacle.x) < radius * 2:
            ball.ball_dx *= -1
            ball.ball_dy *= -1
            global points
            obstacle.strength -= 1
            if obstacle.strength == 0:
                points += 1
                obstacles.remove(obstacle)

        if ball.actor.y >= HEIGHT:
            hearts.pop(len(hearts) - 1)
            ball.actor.x = WIDTH / 2
            ball.actor.y = HEIGHT / 2


def on_mouse_move(pos):
    x, y = pos
    paddle.actor.x = x


pgzrun.go()
