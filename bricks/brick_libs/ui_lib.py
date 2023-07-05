import pygame
from pygame.locals import *
from constants import *
from brick_libs.map_lib import map_library
from brick_libs.game_lib import Game, format_time

class Window:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.NOFRAME)
        self.current_map = map_library['basic']
        self.game = Game(self.win, self.current_map)
        self.selected_map = None
        self.show_map_selection = False
        self.show_start_label = True
        self.game_started = False
        self.map_buttons = {}

        self.arcade_font_path = DEFAULT_FONT
        self.font = pygame.font.Font(self.arcade_font_path, FONT_SIZE)
        self.font_score = pygame.font.Font(self.arcade_font_path, SCORE_FONT_SIZE)
        self.font_life = pygame.font.Font(self.arcade_font_path, LIFE_FONT_SIZE)
        self.font_time = pygame.font.Font(self.arcade_font_path, TIME_FONT_SIZE)
        self.button_font = pygame.font.Font(self.arcade_font_path, BUTTON_FONT_SIZE)
        self.start_label_font = pygame.font.Font(self.arcade_font_path, 100)
        self.start_label = self.start_label_font.render(START_TEXT, True, WHITE)
        self.start_label_rect = self.start_label.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        self.buttons = {
            'Comenzar': {'color': ORANGE, 'rect': pygame.Rect(50, 1100, BUTTON_WIDTH, 50)},
            'Mapa': {'color': GREEN, 'rect': pygame.Rect(50 + BUTTON_WIDTH + BUTTON_SPACING, 1100, BUTTON_WIDTH, 50)},
            'TODO': {'color': PURPLE, 'rect': pygame.Rect(50 + 2*(BUTTON_WIDTH + BUTTON_SPACING), 1100, BUTTON_WIDTH, 50)},
            'Log': {'color': WHITE, 'rect': pygame.Rect(50 + 3*(BUTTON_WIDTH + BUTTON_SPACING), 1100, BUTTON_WIDTH, 50)},
        }

        self.map_selection_buttons = {
            'Aceptar': {'color': GREEN, 'rect': pygame.Rect(350, 650, 100, 50)},
            'Cancelar': {'color': RED, 'rect': pygame.Rect(350, 700, 100, 50)},
        }

        pygame.display.set_caption(TITLE)

    def draw_game_window(self):
        self.win.fill(DARK_GRAY)
        self.draw_top_boxes()
        self.draw_time()
        self.draw_life()
        self.draw_score()
        self.game.draw_game()
        self.draw_buttons()
        self.draw_close_button()
        self.draw_start_text()

    def get_maps(self):
        for i, id in enumerate(map_library.keys()):
            self.map_buttons[id] = {'color': MAP_BUTTON_COLOR, 'rect': pygame.Rect(300, 250 + i *60, 200, 50)}

    def draw_top_boxes(self):
        pygame.draw.rect(self.win, LIGHT_GRAY, (40, 50, 230, 60))
        pygame.draw.rect(self.win, LIGHT_GRAY, (280, 50, 230, 60))
        pygame.draw.rect(self.win, LIGHT_GRAY, (520, 50, 230, 60))

    def draw_time(self):
        time_text = self.font_time.render(f'Tiempo: {format_time(self.game.elapsed_time)}', True, LIGHT_BLUE)
        self.win.blit(time_text, (50, 60))

    def draw_life(self):
        life_text = self.font_life.render('Vidas: 3', True, WHITE)
        self.win.blit(life_text, (290, 60))

    def draw_score(self):
        score_text = self.font_score.render('Score: 0', True, RED)
        self.win.blit(score_text, (530, 60))

    def draw_start_text(self):
        if self.show_start_label:
            self.win.blit(self.start_label, self.start_label_rect)

    def draw_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        for button, info in self.buttons.items():
            if info['rect'].collidepoint(mouse_pos):
                pygame.draw.rect(self.win, info['color'], info['rect'])
                button_text = self.button_font.render(button, True, LIGHT_GRAY)
            else:
                pygame.draw.rect(self.win, LIGHT_GRAY, info['rect'])
                button_text = self.button_font.render(button, True, info['color'])
            button_text_rect = button_text.get_rect(center=info['rect'].center)
            self.win.blit(button_text, button_text_rect)

    def draw_map_selection(self):
        if self.show_map_selection:
            pygame.draw.rect(self.win, LIGHT_GRAY, (250, 200, 300, 600))
            for button, info in self.map_selection_buttons.items():
                pygame.draw.rect(self.win, info['color'], info['rect'])
                button_text = self.button_font.render(button, True, DARK_GRAY)
                button_text_rect = button_text.get_rect(center=info['rect'].center)
                self.win.blit(button_text, button_text_rect)
            for id, info in self.map_buttons.items():
                pygame.draw.rect(self.win, info['color'], info['rect'])
                map_text = self.button_font.render(id, True, DARK_GRAY)
                map_text_rect = map_text.get_rect(center=info['rect'].center)
                self.win.blit(map_text, map_text_rect)

    def draw_close_button(self):
        pygame.draw.rect(self.win, RED, (WINDOW_WIDTH - 50, 0, 50, 50))
        pygame.draw.line(self.win, WHITE, (WINDOW_WIDTH - 40, 10), (WINDOW_WIDTH - 10, 40), 3)
        pygame.draw.line(self.win, WHITE, (WINDOW_WIDTH - 40, 40), (WINDOW_WIDTH - 10, 10), 3)

    def handle_button_click(self, button):
        if button == 'Mapa':
            self.show_map_selection = True
        else:
            print(f'{button} ha sido pulsado')

    def handle_map_selection_click(self, button):
        if button == 'Aceptar':
            if self.selected_map is not None:
                self.current_map = map_library[self.selected_map]
            self.show_map_selection = False
        elif button == 'Cancelar':
            self.show_map_selection = False
        else:
            self.selected_map = button
