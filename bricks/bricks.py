import pygame
from pygame.locals import *
from constants import *
from brick_libs.ball_lib import Ball
from brick_libs.ball_physics import BallPhysics
from brick_libs.brick_lib import set_brick_index, set_brick_size, set_brick_pos
from brick_libs.racket_lib import Racket
from brick_libs.map_lib import map_library
from brick_libs.ui_lib import Window
from brick_libs.game_lib import Game, format_time

play = Window()
play.draw_game_window()
 
#ball_physics = BallPhysics(current_map, current_map.balls[0], current_map.rackets[0], current_map.bricks)

running = True
while running:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and play.show_start_label:
        play.show_start_label = False
        play.game_started = True
        play.game.start_timer()
        #ball_physics.start_movement()

    if play.game_started:
        play.game.update_timer()
        if keys[pygame.K_LEFT]:
            racket_x_position = play.game.map.rackets[0].get_racket_x_pos()
            racket_x_position -= play.game.map.rackets[0].speed
            if racket_x_position < GAME_ZONE_X:
                racket_x_position = GAME_ZONE_X
        if keys[pygame.K_RIGHT]:
            racket_x_position = play.game.map.rackets[0].get_racket_x_pos()
            racket_x_position += play.game.map.rackets[0].speed
            if racket_x_position > GAME_ZONE_X + GAME_ZONE_WIDTH - play.game.map.rackets[0].len:
                racket_x_position = GAME_ZONE_X + GAME_ZONE_WIDTH - play.game.map.rackets[0].len

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x > WINDOW_WIDTH - 50 and y < 50:
                running = False
            elif play.show_map_selection:
                for button, info in play.map_selection_buttons.items():
                    if info['rect'].collidepoint(x, y):
                        play.handle_map_selection_click(button)
                        play.show_start_label = True
                        play.game_started = False
                        play.game.center_racket()
                for id, info in play.map_buttons.items():
                    if info['rect'].collidepoint(x, y):
                        selected_map = id
                        for id, button in play.map_buttons.items():
                            button['color'] = MAP_BUTTON_COLOR if id != selected_map else SELECTED_MAP_BUTTON_COLOR
            else:
                for button, info in play.buttons.items():
                    if info['rect'].collidepoint(x, y):
                        play.handle_button_click(button)
                        play.show_start_label = True
                        play.game_started = False
                        play.game.center_racket()

    #ball_physics.update()
    play.draw_game_window()
    pygame.display.flip()

pygame.quit()
