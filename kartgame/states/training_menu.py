# training_menu.py

import pygame

# importamos los colores de settings.py
from settings import GREEN, WHITE

class TrainingMenu:
    def __init__(self, screen):
        self.screen = screen

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # debes implementar la lógica para cambiar de estado aquí
            pass

    def update(self):
        pass

    def draw(self):
        # dibuja los botones del menú de entrenamiento
        self.screen.fill(GREEN)
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(100, 100, 200, 100))  # botón Carrera
        pygame.draw.rect(self.screen, WHITE, pygame.Rect(500, 100, 200, 100))  # botón Ruedas
        # dibuja los otros botones aquí...
