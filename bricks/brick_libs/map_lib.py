import json

class Map:
    def __init__(self, path: str):
        self.path = path
        map_data = get_map_from_path(path)
        self.color = map_data["color"]
        self.id = map_data["name"]
        self.type = map_data["type"]
        self.bricks = map_data["bricks"]
        self.rackets = map_data["rackets"]
        self.balls = map_data["balls"]

    def __repr__(self):
        return f'Map(id={self.id}, type={self.type}, color={self.color}, bricks={self.bricks}, rackets={self.rackets}, balls={self.balls})'

def get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)

map_basic = Map('./brick_libs/maps/basic.json')
map_fork = Map('./brick_libs/maps/fork.json')
map_chatgpt = Map('./brick_libs/maps/chatgpt.json')
map_triangle = Map('./brick_libs/maps/triangle.json')
map_challenging = Map('./brick_libs/maps/challenging.json')

map_library = {
    map_basic.id: map_basic,
    map_fork.id: map_fork,
    map_chatgpt.id: map_chatgpt,
    map_triangle.id: map_triangle,
    map_challenging.id: map_challenging,
}
