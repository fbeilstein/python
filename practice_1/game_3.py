import pygame
import sys
import math
import random

from vector2d import Vector2D, clamp
from graphics import Ball, Paddle


# -----------------------------
# Collision helper
# -----------------------------
def collide_ball_and_paddle(ball, paddle):
    p, size = paddle.get_sizes()
    sides = [
        [Vector2D(p.x, p.y), Vector2D(p.x + size.x, p.y)],
        [Vector2D(p.x, p.y), Vector2D(p.x, p.y + size.y)],
        [Vector2D(p.x + size.x, p.y), Vector2D(p.x + size.x, p.y + size.y)],
        [Vector2D(p.x + size.x, p.y + size.y), Vector2D(p.x, p.y + size.y)]
    ]
    for p1, p2 in sides:
        if ball.check_collision_and_bounce(p1, p2):
            return True
    return False


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

def reset_game():
    direction = 2 * (random.randint(0, 1) - 0.5)
    angle = (random.random() - 0.5) * 3.0
    ball = Ball(10, (255, 0, 0),
                Vector2D(total_w/2, total_h/2),
                Vector2D(4.0 * math.sin(angle), 4.0 * math.cos(angle) * direction))
    paddle_left = Paddle(Vector2D(30, total_h//2 - 50), Vector2D(20, 100), (0, 0, 255), velocity=5.0,
                         up_key=pygame.K_w, down_key=pygame.K_s, total_w=total_w, total_h=total_h)
    paddle_right = Paddle(Vector2D(total_w - 50, total_h//2 - 50), Vector2D(20, 100), (0, 255, 0), velocity=5.0,
                          up_key=pygame.K_UP, down_key=pygame.K_DOWN, total_w=total_w, total_h=total_h)
    return ball, paddle_left, paddle_right

ball, paddle_left, paddle_right = reset_game()
clock = pygame.time.Clock()

# Add scores
score_left = 0
score_right = 0
WIN_SCORE = 5  # first to 5 wins

while True:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            ball, paddle_left, paddle_right = reset_game()
            score_left, score_right = 0, 0  # reset scores

    # Input
    paddle_left.handle_input(keys)
    paddle_right.handle_input(keys)

    # Collisions with side walls
    ball.check_collision_and_bounce(Vector2D(0, 0), Vector2D(total_w, 0))
    ball.check_collision_and_bounce(Vector2D(0, total_h), Vector2D(total_w, total_h))

    # Top/bottom scoring
    if ball.p.x <= 0:  # Ball passed top edge → bottom player scores
        score_right += 1
        ball, paddle_left, paddle_right = reset_game()
    elif ball.p.x >= total_w:  # Ball passed bottom edge → top player scores
        score_left += 1
        ball, paddle_left, paddle_right = reset_game()

    # Collisions with paddles
    if collide_ball_and_paddle(ball, paddle_left):
        ball.add_to_velocity(paddle_left.get_velocity())
    if collide_ball_and_paddle(ball, paddle_right):
        ball.add_to_velocity(paddle_right.get_velocity())

    # Update objects
    ball.move_and_view(screen)
    paddle_left.move_and_view(screen)
    paddle_right.move_and_view(screen)

    # Draw scores
    score_text = font.render(f"{score_left} : {score_right}", True, BLACK)
    screen.blit(score_text, (total_w//2 - score_text.get_width()//2, 20))

    # Win detection
    if score_left >= WIN_SCORE or score_right >= WIN_SCORE:
        winner = "Left Player" if score_left > score_right else "Right Player"
        win_text = font.render(f"{winner} Wins! Press Enter", True, BLACK)
        screen.blit(win_text, (total_w//2 - win_text.get_width()//2, total_h//2))
        pygame.display.flip()
        continue  # freeze until reset

    pygame.display.flip()
    clock.tick(60)
