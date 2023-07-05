import pygame
from pygame.locals import *
from constants import *
from brick_libs.map_lib import map_library
from brick_libs.brick_lib import brick_library, get_brick_by_id, set_brick_index, set_brick_pos, set_brick_size
from brick_libs.racket_lib import racket_library, get_racket_by_id
from brick_libs.ball_lib import Ball, get_ball_by_id

class Game:
    def __init__(self, win, map):
        self.win = win
        self.map = map
        self.map.bricks = _get_bricks_from_map(map.bricks)
        self.map.rackets = _get_rackets_from_map(map.rackets)
        self.map.balls = _get_balls_from_map(map.balls)
        self.game_zone_x = GAME_ZONE_X
        self.game_zone_y = GAME_ZONE_Y
        self.game_zone_width = GAME_ZONE_WIDTH
        self.game_zone_height = GAME_ZONE_HEIGHT
        self.cols = len(self.map.bricks[0])
        self.rows = len(self.map.bricks)
        self.cell_width = (GAME_ZONE_WIDTH // self.cols)
        self.cell_height = (GAME_ZONE_HEIGHT // self.rows)
        self.map_rect = pygame.Rect(self.game_zone_x, self.game_zone_y, self.game_zone_width, self.game_zone_height)
        self.time = 0
        self.score = 0

    def __repr__(self):
        return f'Game(map={self.map}, game_zone_x={self.game_zone_x}, game_zone_y={self.game_zone_y}, game_zone_width={self.game_zone_width}, game_zone_height={self.game_zone_height}, cols={self.cols}, rows={self.rows}, cell_width={self.cell_width}, cell_height={self.cell_height}, map_rect={self.map_rect}, time={self.time}, score={self.score})'


    def center_racket(self):
        racket = self.map.rackets[0]
        len = racket.len
        self.map.rackets[0].x = (WINDOW_WIDTH - len) // 2
        
    def draw_racket(self):
        racket = self.map.rackets[0]
        racket_color = racket.color
        len = racket.len
        racket.set_racket_size(racket.len, self.cell_height)
        self.map.rackets[0].y = self.map_rect.bottom - self.cell_height

        racket_rect = pygame.Rect(self.map.rackets[0].x, self.map.rackets[0].y, len, self.cell_height)

        pygame.draw.rect(self.win, racket_color, racket_rect)

    def draw_start_ball(self):
        ball = self.map.balls[0]
        ball_radius = ball.radius
        ball_color = ball.color

        ball_x = self.map.rackets[0].x + self.map.rackets[0].len // 2
        ball_y = map_rect.bottom - cell_height - ball_radius

        ball_pos = (ball_x, ball_y)
        set_ball_pos(ball, ball_x, ball_y)

        pygame.draw.circle(self.win, ball_color, ball_pos, ball_radius)

    def draw_ball(self):
        ball = self.map.balls[0]
        ball_radius = ball.radius
        ball_color = ball.color
        ball_pos = ball.get_ball_pos()

        pygame.draw.circle(self.win, ball_color, ball_pos, ball_radius)

    def draw_bricks(self):
        for y in range(self.rows):
            for x in range(self.cols):
                brick = self.map.bricks[y][x]
                if brick is not None:
                    set_brick_index(brick, x, y)
                    set_brick_pos(brick, self.map_rect.left + x * self.cell_width, self.map_rect.top + y * self.cell_height)
                    set_brick_size(brick, self.cell_width, self.cell_height)
                    self.map.bricks[y][x] = brick
                    brick_color = brick.brick_color
                    brick_rect = pygame.Rect(brick.x_left, brick.y_top, brick.width, brick.height)
                    pygame.draw.rect(self.win, brick_color, brick_rect)

    def draw_map(self):
        self.draw_bricks()
        self.draw_racket()
        self.draw_ball()


def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes:02d}:{seconds:02d}'

def _get_bricks_from_map(bricks):
    final_bricks = []
    for row in bricks:
        final_col = []
        for i in row:
            brick = None
            if i != "":
                brick = get_brick_by_id(i)
            final_col.append(brick)
        final_bricks.append(final_col)
    return final_bricks

def _get_rackets_from_map(rackets):
    final_rackets = []
    for i in rackets:
        final_rackets.append(get_racket_by_id(i))
    return final_rackets

def _get_balls_from_map(balls):
    final_balls = []
    for i in balls:
        final_balls.append(get_ball_by_id(i))
    return final_balls