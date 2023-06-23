import pygame
import sys

# inicializamos pygame
pygame.init()

# establecemos el tamaño de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

# colores
white = (255, 255, 255)
blue = (0, 0, 255)

# función para dibujar un botón
def draw_button(x, y, width, height, color, text=''):
    pygame.draw.rect(screen, color, (x, y, width, height))

    if text != '':
        font = pygame.font.Font(None, 50)
        text = font.render(text, True, white)
        screen.blit(text, (x + (width / 2 - text.get_width() / 2), y + (height / 2 - text.get_height() / 2)))

# bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # limpia la pantalla
    screen.fill((0, 0, 0))

    # dibuja los botones
    button_width, button_height = 200, 100
    draw_button(screen_width/2 - button_width - 10, screen_height/2 - button_height - 10, button_width, button_height, blue, 'Jugar')
    draw_button(screen_width/2 + 10, screen_height/2 + 10, button_width, button_height, blue, 'Ajustes')

    # actualiza la pantalla
    pygame.display.flip()
