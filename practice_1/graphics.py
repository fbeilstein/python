
import pygame

import ball
import paddle
from vector2d import Vector2D, clamp


class Ball(ball.Ball):
    def __init__(self, radius, color, pos, velocity, gravity=0.0, clamp_v=True):
        super().__init__(radius, pos, velocity, gravity, clamp_v)
        self.color = color

    def move_and_view(self, surface):
        self.move()
        pygame.draw.circle(surface, self.color, (int(self.p.x), int(self.p.y)), self.r)
        pygame.draw.circle(surface, (0, 0, 0), (int(self.p.x), int(self.p.y)), self.r, 2)


class Paddle(paddle.Paddle):
    def __init__(self, pos, size, color, velocity, up_key=pygame.K_UP, down_key=pygame.K_DOWN, total_w=640, total_h=480):
        super().__init__(pos, size, velocity, total_w, total_h)
        self.color = color
        self.up_key, self.down_key = up_key, down_key

    def handle_input(self, keys):
        self.direction = Vector2D(0, 0)
        if keys[self.up_key]:
            self.direction = Vector2D(0, -1)
        if keys[self.down_key]:
            self.direction = Vector2D(0, 1)

    def move_and_view(self, surface):
        self.move()
        pygame.draw.rect(surface, self.color, (self.p.x, self.p.y, self.size.x, self.size.y))
        pygame.draw.rect(surface, (0, 0, 0), (self.p.x, self.p.y, self.size.x, self.size.y), 2)