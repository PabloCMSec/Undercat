# start_menu.py

import pygame

# importamos los colores de settings.py
from settings import WHITE

class StartMenu:
    def __init__(self, screen):
        self.screen = screen
        self.play_button = pygame.Rect(100, 100, 200, 100)  # botón Jugar
        self.settings_button = pygame.Rect(500, 100, 200, 100)  # botón Ajustes
        self.background = pygame.image.load('media/img/background_menu.png')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()  # obtén las coordenadas del clic del mouse

            if self.play_button.collidepoint(mouse_pos):
                print("¡Has pulsado Jugar!")
            elif self.settings_button.collidepoint(mouse_pos):
                print("¡Has pulsado Ajustes!")

    def update(self):
        pass

    def draw(self):
        # dibuja el fondo
        self.screen.blit(self.background, (0, 0))

        # dibuja los botones del menú de inicio
        pygame.draw.rect(self.screen, WHITE, self.play_button)
        pygame.draw.rect(self.screen, WHITE, self.settings_button)
