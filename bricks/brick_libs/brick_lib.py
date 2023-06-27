class Brick:
    def __init__(self, brick_id:str ,brick_type:str, brick_color:str, points_per_hit:list):
        self.brick_id = brick_id
        self.brick_type = brick_type
        self.brick_color = brick_color
        self.points_per_hit = points_per_hit  # Array con los puntos por cada toque
    
    def __repr__(self):
        return f"Brick(brick_id={self.brick_id}, brick_type={self.brick_type}, brick_color={self.brick_color}, points_per_hit={self.points_per_hit})"

# Crear una biblioteca de bricks
brick_red = Brick('red','normal', (255, 0, 0), [10])
brick_green = Brick('green','normal', (0, 255, 0), [10])
brick_blue = Brick('blue','normal', (0, 0, 255), [10])

brick_library = {
    brick_red.brick_id: brick_red,
    brick_green.brick_id: brick_green,
    brick_blue.brick_id: brick_blue
}

def get_brick_by_id(brick_id:str) -> dict:
    if brick_id in brick_library:
        return brick_library[brick_id]
    else:
        return None
