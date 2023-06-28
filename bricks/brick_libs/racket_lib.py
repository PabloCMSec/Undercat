from constants import *

class Racket:
    def __init__(self, racket_id: str, racket_len: int, color: str, speed: int) -> None:
        self.racket_id = racket_id
        self.racket_len = racket_len  # pixel
        self.color = color
        self.speed = speed  # pixel/s
        self.x = (WINDOW_WIDTH - self.racket_len) // 2  # Posición inicial de la raqueta

    def __repr__(self) -> str:
        return f"Racket(racket_id={self.racket_id}, racket_len={self.racket_len}, color={self.color}, speed={self.speed})"

    def move(self, direction):
        self.x += self.speed * direction
        self.x = max(0, min(WINDOW_WIDTH - self.racket_len, self.x))  # Asegura que la raqueta no se salga de la pantalla

racket_basic = Racket("basic", 112, (255, 128, 0), 10)

racket_library = {
    racket_basic.racket_id : racket_basic
}

def get_racket_by_id(racket_id:str) -> dict:
    if racket_id in racket_library:
        return racket_library[racket_id]
    else:
        return None