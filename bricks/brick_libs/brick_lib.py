import pygame

class Brick:
    def __init__(self, brick_id: str, brick_type: str, brick_color: str, points_per_hit: list):
        self.brick_id = brick_id
        self.brick_type = brick_type
        self.brick_color = brick_color
        self.points_per_hit = points_per_hit
        self.x = 0  # Posición x del ladrillo
        self.y = 0  # Posición y del ladrillo
        self.x_left = 0  # Posición x en pixeles de la esquina superior izquierda
        self.y_top = 0  # Posición y en pixeles de la esquina superior izquierda
        self.width = 0  # Ancho del ladrillo
        self.height = 0  # Altura del ladrillo

    def __repr__(self):
        return f"Brick(brick_id={self.brick_id}, brick_type={self.brick_type}, brick_color={self.brick_color}, points_per_hit={self.points_per_hit}, x={self.x}, y={self.y}, x_left={self.x_left}, y_top={self.y_top}, width={self.width}, height={self.height})"

# Crear una biblioteca de bricks
brick_red = Brick('red', 'normal', (255, 0, 0), [10])
brick_green = Brick('green', 'normal', (0, 255, 0), [10])
brick_blue = Brick('blue', 'normal', (0, 0, 255), [10])

brick_library = {
    brick_red.brick_id: brick_red,
    brick_green.brick_id: brick_green,
    brick_blue.brick_id: brick_blue
}

def get_brick_by_id(brick_id: str) -> Brick:
    if brick_id in brick_library:
        return brick_library[brick_id]
    else:
        return None

def set_brick_index(self, x: int, y: int):
    self.x = x
    self.y = y

def set_brick_pos(self, x_left: int, y_top: int):
    self.x_left = x_left
    self.y_top = y_top

def set_brick_size(self, width: int, height: int):
    self.width = width
    self.height = height
