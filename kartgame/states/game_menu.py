# game_menu.py

import pygame

# importamos los colores de settings.py
from settings import RED, WHITE

class GameMenu:
    def __init__(self, screen):
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # debes implementar la lógica para cambiar de estado aquí
            pass

    def update(self):
        pass

    def draw(self):
        # dibuja los botones del menú del juego
        self.screen.fill(RED)
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(100, 100, 200, 100))  # botón Carrera rápida
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(500, 100, 200, 100))  # botón Entrenamientos
