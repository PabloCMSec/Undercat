import json
from brick_libs.brick_lib import get_brick_by_id

def _get_bricks_from_map(map):
    final_map = []
    for row in map:
        final_col=[]
        for i in row:
            brick = None
            if i != "":
                brick = get_brick_by_id(i)
            final_col.append(brick)
        final_map.append(final_col)
    return final_map

def _get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)

def _fill_map_with_bricks(path:str):
    loaded_map = _get_map_from_path(path)
    loaded_bricks = _get_bricks_from_map(loaded_map['map'])
    loaded_map['map'] = loaded_bricks
    return loaded_map

class Map:
    def __init__(self, map_id:str, map_type:str, map_color:str, map_path:str):
        self.map_id = map_id
        self.map_type = map_type
        self.map_color = map_color
        self.map_path = map_path
        self.map = _fill_map_with_bricks(map_path)

    def __repr__(self):
        return f'Map(id={self.map_id}, map_type={self.map_type}, map_color={self.map_color}, map={self.map})'

map_basic = Map('basic','easy',(47,79,79), './brick_libs/maps/basic.json')
map_fork = Map('fork','easy',(102,0,51), './brick_libs/maps/fork.json')

map_library={
    map_basic.map_id : map_basic,
    map_fork.map_id : map_fork
}