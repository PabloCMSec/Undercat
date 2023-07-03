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
show_start_label = True
game_started = False

racket_x_position = (WINDOW_WIDTH - current_map.map_racket[0].racket_len) // 2

start_label_font = pygame.font.Font(arcade_font_path, 100)
start_label = start_label_font.render("COMENZAR", True, WHITE)
start_label_rect = start_label.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

def center_racket():
    global racket_x_position
    racket = current_map.map_racket[0]
    racket_len = racket.racket_len
    racket_x_position = (WINDOW_WIDTH - racket_len) // 2

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

    if show_start_label:
        win.blit(start_label, start_label_rect)

def draw_racket(map_rect, cell_height):
    global racket_x_position
    racket = current_map.map_racket[0]
    racket_color = racket.color
    racket_len = racket.racket_len

    racket_y_position = map_rect.bottom - cell_height

    racket_rect = pygame.Rect(racket_x_position, racket_y_position, racket_len, cell_height)

    pygame.draw.rect(win, racket_color, racket_rect)

def draw_ball(map_rect, cell_height):
    ball = current_map.map_ball[0]
    ball_color = ball.color
    ball_radius = ball.radius
    ball_x = racket_x_position + current_map.map_racket[0].racket_len // 2
    ball_y = map_rect.bottom - cell_height - ball_radius

    ball_pos = (ball_x, ball_y)

    pygame.draw.circle(win, ball_color, ball_pos, ball_radius)

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
    draw_ball(map_rect, cell_height)

running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and show_start_label:
        show_start_label = False
        game_started = True

    if game_started:
        if keys[pygame.K_LEFT]:
            racket_x_position -= current_map.map_racket[0].speed
            if racket_x_position < 50:
                racket_x_position = 50
        if keys[pygame.K_RIGHT]:
            racket_x_position += current_map.map_racket[0].speed
            if racket_x_position > WINDOW_WIDTH - current_map.map_racket[0].racket_len - 50:
                racket_x_position = WINDOW_WIDTH - current_map.map_racket[0].racket_len - 50

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
                        center_racket()
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
                        center_racket()

    draw_window()
    pygame.display.flip()

pygame.quit()
