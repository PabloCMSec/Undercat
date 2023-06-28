import json
from brick_libs.brick_lib import get_brick_by_id
from brick_libs.racket_lib import get_racket_by_id
from brick_libs.ball_lib import get_ball_by_id

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

def _get_rackets_from_map(map):
    rackets = []
    for i in map:
        rackets.append(get_racket_by_id(i))
    return rackets

def _get_balls_from_map(map):
    balls = []
    for i in map:
        balls.append(get_ball_by_id(i))
    return balls

def _get_map_from_path(path: str):
    with open(path) as file:
        return json.load(file)

def _fill_map(path:str):
    loaded_map = _get_map_from_path(path)
    loaded_bricks = _get_bricks_from_map(loaded_map['map'])
    loaded_rackets = _get_rackets_from_map(loaded_map['racket'])
    loaded_balls = _get_balls_from_map(loaded_map['ball'])
    loaded_map['map'] = loaded_bricks
    loaded_map['racket'] = loaded_rackets
    loaded_map['ball'] = loaded_balls
    return loaded_map

class Map:
    def __init__(self, map_id:str, map_type:str, map_color:str, map_path:str):
        self.map_id = map_id
        self.map_type = map_type
        self.map_color = map_color
        self.map_path = map_path
        filled_map = _fill_map(map_path)
        self.map = filled_map["map"]
        self.map_racket = filled_map["racket"]
        self.map_ball = filled_map["ball"]

    def __repr__(self):
        return f'Map(id={self.map_id}, map_type={self.map_type}, map_color={self.map_color}, map={self.map}, map_racket={self.map_racket}, map_ball={self.map_ball})'

map_basic = Map('basic','easy',(47,79,79), './brick_libs/maps/basic.json')
map_fork = Map('fork','easy',(51,0,25), './brick_libs/maps/fork.json')

map_library={
    map_basic.map_id : map_basic,
    map_fork.map_id : map_fork
}