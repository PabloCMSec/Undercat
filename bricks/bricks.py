import pygame
import time
from pygame.locals import *
from constants import *
from brick_libs.ui_lib import (draw_buttons, draw_map_selection, draw_close_button,
                               handle_button_click, handle_map_selection_click,
                               buttons, map_selection_buttons, map_buttons)
from brick_libs.game_lib import (center_racket, format_time, draw_racket, draw_start_ball,
                                draw_ball, draw_bricks)
from brick_libs.map_lib import map_library
from brick_libs.ball_lib import Ball
from brick_libs.brick_lib import set_brick_index, set_brick_size, set_brick_pos
from brick_libs.racket_lib import set_racket_pos, set_racket_size
from brick_libs.ball_physics import BallPhysics

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
ball = current_map.map_ball[0]

selected_map = None
show_map_selection = False
show_start_label = True
game_started = False
start_time = 0
elapsed_time = 0

racket_x_position = (WINDOW_WIDTH - current_map.map_racket[0].racket_len) // 2

start_label_font = pygame.font.Font(arcade_font_path, 100)
start_label = start_label_font.render("COMENZAR", True, WHITE)
start_label_rect = start_label.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

def draw_window():
    win.fill(DARK_GRAY)

    pygame.draw.rect(win, LIGHT_GRAY, (40, 50, 230, 60))
    pygame.draw.rect(win, LIGHT_GRAY, (280, 50, 230, 60))
    pygame.draw.rect(win, LIGHT_GRAY, (520, 50, 230, 60))

    time_text = font_time.render(f'Tiempo: {format_time(elapsed_time)}', True, LIGHT_BLUE)
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

    if show_start_label:
        win.blit(start_label, start_label_rect)

def draw_map():
    rows = len(current_map.map)
    cols = len(current_map.map[0])
    cell_width = (GAME_ZONE_WIDTH // cols)
    cell_height = (GAME_ZONE_HEIGHT // rows)

    map_rect = pygame.Rect(GAME_ZONE_X, GAME_ZONE_Y, GAME_ZONE_WIDTH, GAME_ZONE_HEIGHT)

    draw_bricks(win, current_map, map_rect)
    draw_racket(win, racket_x_position,current_map.map_racket[0], map_rect, cell_height)
    draw_start_ball(win, racket_x_position, current_map.map_ball[0], current_map, map_rect, cell_height)
   
ball_physics = BallPhysics(current_map, ball, current_map.map_racket[0], current_map.map)

running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and show_start_label:
        show_start_label = False
        game_started = True
        start_time = time.time()
        ball_physics.start_movement()

    if game_started:
        elapsed_time = int(time.time() - start_time)
        if keys[pygame.K_LEFT]:
            racket_x_position -= current_map.map_racket[0].speed
            if racket_x_position < GAME_ZONE_X:
                racket_x_position = GAME_ZONE_X
        if keys[pygame.K_RIGHT]:
            racket_x_position += current_map.map_racket[0].speed
            if racket_x_position > GAME_ZONE_X + GAME_ZONE_WIDTH - current_map.map_racket[0].racket_len:
                racket_x_position = GAME_ZONE_X + GAME_ZONE_WIDTH - current_map.map_racket[0].racket_len

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
                        show_start_label = True
                        game_started = False
                        racket_x_position = center_racket(racket_x_position,current_map.map_racket[0])
                for map_id, info in map_buttons.items():
                    if info['rect'].collidepoint(x, y):
                        selected_map = map_id
                        for id, button in map_buttons.items():
                            button['color'] = MAP_BUTTON_COLOR if id != selected_map else SELECTED_MAP_BUTTON_COLOR
            else:
                for button, info in buttons.items():
                    if info['rect'].collidepoint(x, y):
                        show_map_selection = handle_button_click(buttons, button)
                        show_start_label = True
                        game_started = False
                        racket_x_position = center_racket(racket_x_position,current_map.map_racket[0])


    ball_physics.update()  # Actualizar la posición de la bola
    draw_window()
    pygame.display.flip()

pygame.quit()
