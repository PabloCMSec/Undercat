import json
from brick_libs.brick_lib import brick_library

def _get_map_from_path(path: str):
    with open(path) as path:
        return json.load(path)
    
class Map:
    def __init__(self, map_id, map_type, map_color, map_path):
        self.map_id = map_id
        self.map_type = map_type
        self.map_color = map_color
        self.map_path = map_path
        self.map = _get_map_from_path(map_path)
    

map_basic = Map('basic','easy',(47,79,79), './brick_libs/maps/basic.json')

map_library={
    map_basic.map_id : map_basic
}
