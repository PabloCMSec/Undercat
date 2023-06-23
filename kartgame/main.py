# main.py

import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from states.start_menu import StartMenu
from states.game_menu import GameMenu
from states.training_menu import TrainingMenu
from states.ruedas_game import RuedasGame

def main():
    pygame.init()
    pygame.display.set_caption("Undercat Kart Game")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Crea los estados del juego
    states = {
        "START": StartMenu(screen),
        "GAME": GameMenu(screen),
        "TRAINING": TrainingMenu(screen),
        "RUEDAS": RuedasGame(screen)
    }

    # Estado inicial
    state = states["START"]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                state.handle_event(event)

            # Aquí necesitarás implementar la lógica para cambiar entre estados
            # Por ejemplo, puedes cambiar al estado de juego cuando el usuario
            # hace clic en el botón de jugar en el menú de inicio:
            # if state is states["START"] and state.play_button_pressed:
            #     state = states["GAME"]

        state.update()
        state.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
