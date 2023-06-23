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

# estados de la aplicación
states = ['start', 'game_menu', 'training_menu']
state_index = 0

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

        # manejo de eventos de click para cambiar de estado
        if event.type == pygame.MOUSEBUTTONDOWN:
            if states[state_index] == 'start':
                state_index = 1  # cambiamos al estado de 'game_menu'
            elif states[state_index] == 'game_menu':
                state_index = 2  # cambiamos al estado de 'training_menu'
            elif states[state_index] == 'training_menu':
                state_index = 0  # volvemos al estado de 'start'

    # limpia la pantalla
    screen.fill((0, 0, 0))

    # dibuja los botones dependiendo del estado actual
    button_width, button_height = 200, 100
    if states[state_index] == 'start':
        draw_button(screen_width/2 - button_width - 10, screen_height/2 - button_height - 10, button_width, button_height, blue, 'Jugar')
        draw_button(screen_width/2 + 10, screen_height/2 + 10, button_width, button_height, blue, 'Ajustes')
    elif states[state_index] == 'game_menu':
        draw_button(screen_width/2 - button_width - 10, screen_height/2 - button_height - 10, button_width, button_height, blue, 'Carrera rápida')
        draw_button(screen_width/2 + 10, screen_height/2 + 10, button_width, button_height, blue, 'Entrenamientos')
    elif states[state_index] == 'training_menu':
        draw_button(screen_width/2 - button_width - 10, screen_height/2 - button_height - 10, button_width, button_height, blue, 'Carrera')
        draw_button(screen_width/2 + 10, screen_height/2 + 10, button_width, button_height, blue, 'Ruedas')

    # actualiza la pantalla
    pygame.display.flip()
