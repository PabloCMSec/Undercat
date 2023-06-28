import pygame
from pygame.locals import *
from constants import *
from brick_libs.map_lib import map_library

buttons = {
    'Comenzar': {'color': ORANGE, 'rect': pygame.Rect(50, 1100, BUTTON_WIDTH, 50)},
    'Mapa': {'color': GREEN, 'rect': pygame.Rect(50 + BUTTON_WIDTH + BUTTON_SPACING, 1100, BUTTON_WIDTH, 50)},
    'TODO': {'color': PURPLE, 'rect': pygame.Rect(50 + 2*(BUTTON_WIDTH + BUTTON_SPACING), 1100, BUTTON_WIDTH, 50)},
    'Log': {'color': WHITE, 'rect': pygame.Rect(50 + 3*(BUTTON_WIDTH + BUTTON_SPACING), 1100, BUTTON_WIDTH, 50)},
}

map_selection_buttons = {
    'Aceptar': {'color': GREEN, 'rect': pygame.Rect(350, 650, 100, 50)},
    'Cancelar': {'color': RED, 'rect': pygame.Rect(350, 700, 100, 50)},
}

map_buttons = {}
for i, map_id in enumerate(map_library.keys()):
    map_buttons[map_id] = {'color': MAP_BUTTON_COLOR, 'rect': pygame.Rect(300, 250 + i * 60, 200, 50)}


def draw_buttons(win, buttons, button_font):
    mouse_pos = pygame.mouse.get_pos()
    for button, info in buttons.items():
        if info['rect'].collidepoint(mouse_pos):
            pygame.draw.rect(win, info['color'], info['rect'])
            button_text = button_font.render(button, True, LIGHT_GRAY)
        else:
            pygame.draw.rect(win, LIGHT_GRAY, info['rect'])
            button_text = button_font.render(button, True, info['color'])
        button_text_rect = button_text.get_rect(center=info['rect'].center)
        win.blit(button_text, button_text_rect)

def draw_map_selection(win, show_map_selection, map_selection_buttons, map_buttons, button_font):
    if show_map_selection:
        pygame.draw.rect(win, LIGHT_GRAY, (250, 200, 300, 600))
        for button, info in map_selection_buttons.items():
            pygame.draw.rect(win, info['color'], info['rect'])
            button_text = button_font.render(button, True, DARK_GRAY)
            button_text_rect = button_text.get_rect(center=info['rect'].center)
            win.blit(button_text, button_text_rect)
        for map_id, info in map_buttons.items():
            pygame.draw.rect(win, info['color'], info['rect'])
            map_text = button_font.render(map_id, True, DARK_GRAY)
            map_text_rect = map_text.get_rect(center=info['rect'].center)
            win.blit(map_text, map_text_rect)

def draw_close_button(win):
    pygame.draw.rect(win, RED, (WINDOW_WIDTH - 50, 0, 50, 50))
    pygame.draw.line(win, WHITE, (WINDOW_WIDTH - 40, 10), (WINDOW_WIDTH - 10, 40), 3)
    pygame.draw.line(win, WHITE, (WINDOW_WIDTH - 40, 40), (WINDOW_WIDTH - 10, 10), 3)

def handle_button_click(buttons, button):
    if button == 'Mapa':
        show_map_selection = True
        return show_map_selection
    else:
        print(f'{button} ha sido pulsado')

def handle_map_selection_click(map_selection_buttons, map_buttons, button, current_map, selected_map, map_library):
    if button == 'Aceptar':
        if selected_map is not None:
            current_map = map_library[selected_map]
            print(current_map)  # Imprime el mapa que se ha cargado
        show_map_selection = False
    elif button == 'Cancelar':
        show_map_selection = False
    else:
        selected_map = button
        for id, button in map_buttons.items():
            button['color'] = MAP_BUTTON_COLOR if id != selected_map else SELECTED_MAP_BUTTON_COLOR

    return current_map, selected_map, show_map_selection
