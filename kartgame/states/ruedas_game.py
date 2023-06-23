# ruedas_game.py

import pygame
from settings import YELLOW, RED, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT

class RuedasGame:
    def __init__(self, screen):
        self.screen = screen
        self.white_circle_x = SCREEN_WIDTH / 2
        self.white_circle_speed = 2

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                self.white_circle_speed = 0

    def update(self):
        self.white_circle_x += self.white_circle_speed
        if self.white_circle_x > SCREEN_WIDTH or self.white_circle_x < 0:
            self.white_circle_speed *= -1

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.line(self.screen, YELLOW, (0, SCREEN_HEIGHT / 2), (SCREEN_WIDTH, SCREEN_HEIGHT / 2), 5)
        pygame.draw.circle(self.screen, RED, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2), 50)
        pygame.draw.circle(self.screen, WHITE, (int(self.white_circle_x), SCREEN_HEIGHT / 2), 50)
