import pygame
from pygame.locals import *
from constants import *
from brick_libs.map_lib import map_library

def center_racket(racket_x_position,racket):
    racket_len = racket.racket_len
    racket_x_position = (WINDOW_WIDTH - racket_len) // 2

def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes:02d}:{seconds:02d}'