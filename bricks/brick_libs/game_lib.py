import pygame
from pygame.locals import *
from constants import *
from brick_libs.map_lib import map_library
from brick_libs.racket_lib import racket_library, set_racket_pos, set_racket_size


def center_racket(racket_x_position,racket):
    racket_len = racket.racket_len
    racket_x_position = (WINDOW_WIDTH - racket_len) // 2
    return racket_x_position

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes:02d}:{seconds:02d}'

def draw_racket(win, racket_x_position, racket, map_rect, cell_height):
    racket_color = racket.color
    racket_len = racket.racket_len
    set_racket_size(racket,racket_len,cell_height)
    racket_y_position = map_rect.bottom - cell_height

    racket_rect = pygame.Rect(racket_x_position, racket_y_position, racket_len, cell_height)

    pygame.draw.rect(win, racket_color, racket_rect)

def draw_start_ball(win, racket_x_position, ball, current_map, map_rect, cell_height):
    ball_radius = ball.radius
    ball_color = ball.color

    ball_x = racket_x_position + current_map.map_racket[0].racket_len // 2
    ball_y = map_rect.bottom - cell_height - ball_radius

    ball_pos = (ball_x, ball_y)

    pygame.draw.circle(win, ball_color, ball_pos, ball_radius)