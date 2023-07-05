from constants import *

class Racket:
    def __init__(self, id: str, len: int, color: str, speed: float):
        self.id = id
        self.len = len  # pixel
        self.color = color
        self.speed = speed  # pixel/s
        self.x = (WINDOW_WIDTH - self.len) // 2  # Posición inicial de la raqueta
        self.y = 0  # Posición y del ladrillo
        self.width = 0  # Ancho del ladrillo
        self.height = 0  # Altura del ladrillo

    def __repr__(self) -> str:
        return f"Racket(id={self.id}, len={self.len}, color={self.color}, speed={self.speed}, x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def move(self, direction):
        self.x += self.speed * direction
        self.x = max(GAME_ZONE_X, min(GAME_ZONE_X + GAME_ZONE_WIDTH - self.len, self.x))

    def set_racket_size(self, width: int, height: int):
        self.width = width
        self.height = height

    def set_racket_x_pos(self, x_left: int):
        self.x_left = x_left

    def get_racket_x_pos(self):
        return self.x

racket_basic = Racket("basic", 112, (255, 128, 0), 1)

racket_library = {
    racket_basic.id : racket_basic
}

def get_racket_by_id(id:str) -> dict:
    if id in racket_library:
        return racket_library[id]
    else:
        return None
