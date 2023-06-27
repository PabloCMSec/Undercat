class Brick:
    def __init__(self, brick_type, color, points_per_hit):
        self.brick_type = brick_type
        self.color = color
        self.points_per_hit = points_per_hit  # Array con los puntos por cada toque

# Crear una biblioteca de bricks
brick_library = {
    "id1": Brick('normal', (255, 0, 0), [10]),
    "id2": Brick('normal', (0, 255, 0), [10]),
    "id3": Brick('normal', (0, 0, 255), [10])
}