# utils.py

import pygame

def load_image(image_path):
    """Carga una imagen desde el archivo especificado."""
    return pygame.image.load(image_path)

def play_sound(sound_path):
    """Reproduce un sonido desde el archivo especificado."""
    pygame.mixer.Sound(sound_path).play()

def calculate_score(points_per_hit, hits):
    """Calcula la puntuación total basada en los puntos por cada golpe y el número de golpes."""
    return points_per_hit * hits
