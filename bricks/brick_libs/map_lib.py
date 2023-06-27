import json
from brick_libs.brick_lib import get_brick_by_id

def _get_bricks_from_map(map):
    final_map = []
    for row in map:
        final_col=[]
        for i in row:
            final_col.append(get_brick_by_id(i))
        final_map.append(final_col)
    return final_map  # Devuelve la matriz final de ladrillos

def _get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)
    
def _fill_map_with_bricks(path:str):
    loaded_map = _get_map_from_path(path)
    loaded_bricks = _get_bricks_from_map(loaded_map['map'])  # Accede a la clave 'map'
    loaded_map['map'] = loaded_bricks  # Asigna loaded_bricks a la clave 'map'
    return loaded_map['map']  # Devuelve la matriz de ladrillos

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

map_library={
    map_basic.map_id : map_basic
}
