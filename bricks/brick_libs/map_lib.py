import json

class Map:
    def __init__(self, id:str, type:str, color:str, path:str):
        self.id = id
        self.color = color
        self.path = path
        map = _get_map_from_path(path)
        self.type = map["type"]
        self.bricks = map["bricks"]
        self.rackets = map["rackets"]
        self.balls = map["balls"]

    def __repr__(self):
        return f'Map(id={self.id}, type={self.type}, color={self.color}, bricks={self.bricks}, rackets={self.rackets}, balls={self.balls})'

def _get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)

map_basic = Map('basic','easy',(47,79,79), './brick_libs/maps/basic.json')
map_fork = Map('fork','easy',(51,0,25), './brick_libs/maps/fork.json')

map_library={
    map_basic.id : map_basic,
    map_fork.id : map_fork
}