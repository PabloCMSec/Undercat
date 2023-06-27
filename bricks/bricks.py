import pygame
from pygame.locals import *
from brick_libs.brick_lib import brick_library
from brick_libs.map_lib import map_library

pygame.init()

win = pygame.display.set_mode((800, 1200))
pygame.display.set_caption('Bricks AI')  # Título de la ventana

font = pygame.font.Font(None, 30)
button_font = pygame.font.Font(None, 25)

# Define los colores
white = (255, 255, 255)
dark_gray = (200, 200, 200)
light_gray = (70, 70, 70)
red = (255, 0, 0)
light_blue = (173, 216, 230)
orange = (255, 165, 0)
green = (0, 255, 0)
purple = (128, 0, 128)

# Ajustado para mantener la misma distancia entre los botones
button_spacing = 30
button_width = 150
buttons = {
    'Comenzar': {'color': orange, 'rect': pygame.Rect(50, 1100, button_width, 50)},
    'Mapa': {'color': green, 'rect': pygame.Rect(50 + button_width + button_spacing, 1100, button_width, 50)},
    'TODO': {'color': purple, 'rect': pygame.Rect(50 + 2*(button_width + button_spacing), 1100, button_width, 50)},
    'Log': {'color': white, 'rect': pygame.Rect(50 + 3*(button_width + button_spacing), 1100, button_width, 50)},
}

# Referencia al mapa básico
current_map = map_library['basic']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button, info in buttons.items():
                if info['rect'].collidepoint(x, y):
                    if button == 'Mapa':
                        print(map_library)  # Imprime la biblioteca de mapas cuando se presiona el botón de mapa
                    else:
                        print(f'{button} ha sido pulsado')

    # Llena el fondo con gris oscuro
    win.fill(dark_gray)

    # Dibuja las cajas de tiempo, vidas y puntuación.
    pygame.draw.rect(win, light_gray, (50, 50, 200, 50))
    pygame.draw.rect(win, light_gray, (300, 50, 200, 50))  # Nuevo cuadro de vidas
    pygame.draw.rect(win, light_gray, (550, 50, 200, 50))

    # Dibuja el texto en las cajas.
    time_text = font.render('Tiempo: 00:00', True, light_blue)
    lives_text = font.render('Vidas: 3', True, white)  # Nuevo texto de vidas
    score_text = font.render('Puntuación: 0', True, red)
    win.blit(time_text, (60, 60))
    win.blit(lives_text, (310, 60))  # Dibuja el nuevo texto de vidas
    win.blit(score_text, (560, 60))

    # Dibuja el cuadro de juego con el color del mapa actual
    pygame.draw.rect(win, current_map.map_color, (50, 150, 700, 900))

    # Dibuja los botones.
    mouse_pos = pygame.mouse.get_pos()
    for button, info in buttons.items():
        if info['rect'].collidepoint(mouse_pos):
            # Invierte los colores si el ratón está encima
            pygame.draw.rect(win, info['color'], info['rect'])
            button_text = button_font.render(button, True, light_gray)
        else:
            pygame.draw.rect(win, light_gray, info['rect'])
            button_text = button_font.render(button, True, info['color'])

        # Dibuja el texto del botón
        button_text_rect = button_text.get_rect(center=info['rect'].center)
        win.blit(button_text, button_text_rect)

    pygame.display.flip()

pygame.quit()
