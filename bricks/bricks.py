import pygame
from pygame.locals import *
from constants import *
from brick_libs.ui_lib import (draw_buttons, draw_map_selection, draw_close_button,
                               handle_button_click, handle_map_selection_click,
                               buttons, map_selection_buttons, map_buttons)
from brick_libs.map_lib import map_library

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption('Bricks AI')

arcade_font_path = 'media/fonts/arcade.ttf'
font = pygame.font.Font(arcade_font_path, FONT_SIZE)
font_score = pygame.font.Font(arcade_font_path, SCORE_FONT_SIZE)
font_life = pygame.font.Font(arcade_font_path, LIFE_FONT_SIZE)
font_time = pygame.font.Font(arcade_font_path, TIME_FONT_SIZE)
button_font = pygame.font.Font(arcade_font_path, BUTTON_FONT_SIZE)

current_map = map_library['basic']
selected_map = None
show_map_selection = False

def draw_window():
    win.fill(DARK_GRAY)

    pygame.draw.rect(win, LIGHT_GRAY, (40, 50, 230, 60))
    pygame.draw.rect(win, LIGHT_GRAY, (280, 50, 230, 60))
    pygame.draw.rect(win, LIGHT_GRAY, (520, 50, 230, 60))

    time_text = font_time.render('Tiempo: 00:00', True, LIGHT_BLUE)
    lives_text = font_life.render('Vidas: 3', True, WHITE)
    score_text = font_score.render('Score: 0', True, RED)
    win.blit(time_text, (50, 60))
    win.blit(lives_text, (290, 60))
    win.blit(score_text, (530, 60))

    pygame.draw.rect(win, current_map.map_color, (50, 150, 700, 900))
    draw_map()

    draw_buttons(win, buttons, button_font)
    draw_map_selection(win, show_map_selection, map_selection_buttons, map_buttons, button_font)
    draw_close_button(win)

def draw_racket(map_rect, cell_height):
    racket = current_map.map_racket[0]
    racket_color = racket.color
    racket_len = racket.racket_len  # Esta es la longitud de tu raqueta
    racket_x_position = racket.x  # Esta es la posición horizontal de tu raqueta

    racket_y_position = map_rect.bottom - cell_height

    racket_rect = pygame.Rect(racket_x_position, racket_y_position, racket_len, cell_height)

    pygame.draw.rect(win, racket_color, racket_rect)



def draw_map():
    rows = len(current_map.map)
    cols = len(current_map.map[0])
    cell_width = 700 // cols
    cell_height = 900 // rows

    map_rect = pygame.Rect(50, 150, 700, 900)

    for y in range(rows):
        for x in range(cols):
            brick = current_map.map[y][x]
            if brick is not None:
                brick_color = brick.brick_color
                brick_rect = pygame.Rect(map_rect.left + x * cell_width, map_rect.top + y * cell_height, cell_width, cell_height)
                pygame.draw.rect(win, brick_color, brick_rect)
    draw_racket(map_rect, cell_height)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Nuevo código
            if event.key == pygame.K_LEFT:  # Si se presiona la flecha izquierda
                current_map.map_racket[0].move(-1)  # Mover la raqueta a la izquierda
            elif event.key == pygame.K_RIGHT:  # Si se presiona la flecha derecha
                current_map.map_racket[0].move(1)  # Mover la raqueta a la derecha
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > WINDOW_WIDTH - 50 and y < 50:
                running = False
            elif show_map_selection:
                for button, info in map_selection_buttons.items():
                    if info['rect'].collidepoint(x, y):
                        current_map, selected_map, show_map_selection = handle_map_selection_click(map_selection_buttons, map_buttons, button, current_map, selected_map, map_library)
                for map_id, info in map_buttons.items():
                    if info['rect'].collidepoint(x, y):
                        selected_map = map_id
                        for id, button in map_buttons.items():
                            button['color'] = MAP_BUTTON_COLOR if id != selected_map else SELECTED_MAP_BUTTON_COLOR
            else:
                for button, info in buttons.items():
                    if info['rect'].collidepoint(x, y):
                        show_map_selection = handle_button_click(buttons, button)

    draw_window()
    pygame.display.flip()

pygame.quit()