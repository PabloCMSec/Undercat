import pygame
from pygame.math import Vector2
from constants import WINDOW_WIDTH, WINDOW_HEIGHT

class BallPhysics:
    def __init__(self, map, ball, racket, bricks):
        self.ball = ball
        self.map = map
        self.racket = racket
        self.bricks = bricks
        self.velocity = Vector2(0, 0)
        self.is_moving = False

    def start_movement(self):
        self.velocity = Vector2(0, -self.ball.speed)
        self.is_moving = True

    def update(self):
        if self.is_moving:
            self.ball.position += self.velocity

            # Collisions
            self.check_wall_collision()
            self.check_racket_collision()
            self.check_brick_collision()

    def check_wall_collision(self):
        if self.ball.position.x - self.ball.radius <= 0 or self.ball.position.x + self.ball.radius >= WINDOW_WIDTH:
            self.velocity.x *= -1

        if self.ball.position.y - self.ball.radius <= 0:
            self.velocity.y *= -1

    def check_racket_collision(self):
        racket_rect = pygame.Rect(self.racket.x, self.racket.y, self.racket.width, self.racket.height)
        if self.ball.rect.colliderect(racket_rect):
            self.velocity.y *= -1

    def check_brick_collision(self):
        for row in range(len(self.map.map)):
            for col in range(len(self.map.map[row])):
                brick = self.map.map[row][col]
                if brick is not None:
                    brick_rect = pygame.Rect(brick.x, brick.y, brick.width, brick.height)
                    if self.ball.rect.colliderect(brick_rect):
                        self.map.map[row][col] = None
                        self.ball.velocity.y *= -1  # Invertir la dirección vertical de la bola
                        # Realizar acciones adicionales según las características del ladrillo (puntos, efectos, etc.)
