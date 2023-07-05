import pygame

class Ball:
    def __init__(self, ball_id: str, radius: int, color: str, speed: int):
        self.ball_id = ball_id
        self.radius = radius
        self.color = color
        self.speed = speed
        self.position = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(0, 0, radius * 2, radius * 2)

    def __repr__(self):
        return f"Ball(ball_id={self.ball_id}, radius={self.radius}, color={self.color}, speed={self.speed})"

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position  # Actualizar el rectángulo de colisión

    def set_ball_pos(self, x ,y):
        self.position = pygame.Vector2(x, y)

def get_ball_pos(self):
    x = self.position.x
    y = self.position.y
    return x, y

def get_ball_x_pos(self):
    x = self.position.x
    return x

def get_ball_y_pos(self):
    y = self.position.y
    return y

ball_basic = Ball("basic", 10, (255, 204, 255), 5)

ball_library = {
    ball_basic.ball_id: ball_basic
}

def get_ball_by_id(ball_id: str) -> dict:
    if ball_id in ball_library:
        return ball_library[ball_id]
    else:
        return None
