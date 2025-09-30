import pygame
import sys
import math
import random

from vector2d import Vector2D, clamp
from graphics import Ball




# -----------------------------
# Main game loop
# -----------------------------
pygame.init()
total_w, total_h = 1000, 600
screen = pygame.display.set_mode((total_w, total_h))
pygame.display.set_caption("Ping-Pong with Score")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
font = pygame.font.SysFont(None, 48)



direction = 2 * (random.randint(0, 1) - 0.5)
angle = (random.random() - 0.5) * 3.0
ball = Ball(10, (255, 0, 0),
            Vector2D(total_w/2, total_h/2),
            Vector2D(4.0 * math.sin(angle), 4.0 * math.cos(angle) * direction), 
            gravity=-0.2, clamp_v=False)
clock = pygame.time.Clock()


while True:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
   

    # Collisions with side walls
    ball.check_collision_and_bounce(Vector2D(0, 0), Vector2D(total_w, 0))
    ball.check_collision_and_bounce(Vector2D(0, total_h), Vector2D(total_w, total_h))
    ball.check_collision_and_bounce(Vector2D(0, 0), Vector2D(0, total_h))
    ball.check_collision_and_bounce(Vector2D(total_w, 0), Vector2D(total_w, total_h))

    if ball.p.y > total_h:
        ball.v.y = - ball.v.y
    if ball.p.y < 0:
        ball.v.y = - ball.v.y

    # Update objects
    ball.move_and_view(screen)


    pygame.display.flip()
    clock.tick(60)
