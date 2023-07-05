import json

class Map:
    def __init__(self, map_id:str, map_type:str, map_color:str, map_path:str):
        self.map_id = map_id
        self.map_color = map_color
        self.map_path = map_path
        map = _get_map_from_path(map_path)
        self.map_type = map["type"]
        self.bricks = map["bricks"]
        self.rackets = map["rackets"]
        self.balls = map["balls"]

    def __repr__(self):
        return f'Map(id={self.map_id}, map_type={self.map_type}, map_color={self.map_color}, bricks={self.bricks}, rackets={self.rackets}, balls={self.balls})'

def _get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)

map_basic = Map('basic','easy',(47,79,79), './brick_libs/maps/basic.json')
map_fork = Map('fork','easy',(51,0,25), './brick_libs/maps/fork.json')

map_library={
    map_basic.map_id : map_basic,
    map_fork.map_id : map_fork
}