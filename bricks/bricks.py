import pygame
from pygame.locals import *

from brick_libs.brick_lib import brick_library, get_brick_by_id
from brick_libs.map_lib import map_library
from brick_libs.ui_lib import (draw_buttons, draw_map_selection, draw_close_button, 
                               handle_button_click, handle_map_selection_click, 
                               buttons, map_selection_buttons, map_buttons)

from constants import *
from utils import load_image, play_sound, calculate_score

pygame.init()

win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
pygame.display.set_caption('Bricks AI')

arcade_font_path = 'media/fonts/source/arcade.ttf'
font = pygame.font.Font(arcade_font_path, FONT_SIZE)
button_font = pygame.font.Font(arcade_font_path, BUTTON_FONT_SIZE)

current_map = map_library['basic']  
selected_map = None  
show_map_selection = False  

def draw_window():
    win.fill(DARK_GRAY)

    pygame.draw.rect(win, LIGHT_GRAY, (50, 50, 200, 50))
    pygame.draw.rect(win, LIGHT_GRAY, (300, 50, 200, 50))
    pygame.draw.rect(win, LIGHT_GRAY, (550, 50, 200, 50))

    time_text = font.render('Tiempo: 00:00', True, LIGHT_BLUE)
    lives_text = font.render('Vidas: 3', True, WHITE)
    score_text = font.render('Score: 0', True, RED)
    win.blit(time_text, (60, 60))
    win.blit(lives_text, (310, 60))
    win.blit(score_text, (560, 60))

    pygame.draw.rect(win, current_map.map_color, (50, 150, 700, 900))

    draw_buttons(win, buttons, button_font)
    draw_map_selection(win, show_map_selection, map_selection_buttons, map_buttons, button_font)
    draw_close_button(win)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
