from constants import *

class Racket:
    def __init__(self, racket_id: str, racket_len: int, color: str, speed: float) -> None:
        self.racket_id = racket_id
        self.racket_len = racket_len  # pixel
        self.color = color
        self.speed = speed  # pixel/s
        self.x = (WINDOW_WIDTH - self.racket_len) // 2  # Posición inicial de la raqueta
        self.y = 0  # Posición y del ladrillo
        self.width = 0  # Ancho del ladrillo
        self.height = 0  # Altura del ladrillo

    def __repr__(self) -> str:
        return f"Racket(racket_id={self.racket_id}, racket_len={self.racket_len}, color={self.color}, speed={self.speed}, x={self.x}, y={self.y}, width={self.width}, height={self.height})"

    def move(self, direction):
        self.x += self.speed * direction
        self.x = max(GAME_ZONE_X, min(GAME_ZONE_X + GAME_ZONE_WIDTH - self.racket_len, self.x))

racket_basic = Racket("basic", 112, (255, 128, 0), 1)

racket_library = {
    racket_basic.racket_id : racket_basic
}

def get_racket_by_id(racket_id:str) -> dict:
    if racket_id in racket_library:
        return racket_library[racket_id]
    else:
        return None

def set_racket_pos(self, x_left: int, y_top: int):
    self.x_left = x_left
    self.y_top = y_top

def set_racket_size(self, width: int, height: int):
    self.width = width
    self.height = height
