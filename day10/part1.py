from dataclasses import dataclass
from time import sleep

file = open('day10/input.txt', 'r')
lines = file.read().splitlines()


@dataclass
class PipePoint:
    char: str
    north: bool = False
    east: bool = False
    south: bool = False
    west: bool = False
    start: bool = False
    dist: int = 0

    def __init__(self, char: str):
        self.char = char
        match char:
            case '|':
                self.north = True
                self.south = True
            case '-':
                self.east = True
                self.west = True
            case 'L':
                self.north = True
                self.east = True
            case 'J':
                self.north = True
                self.west = True
            case '7':
                self.south = True
                self.west = True
            case 'F':
                self.east = True
                self.south = True
            case 'S':
                self.start = True
                self.north = True
                self.east = True
                self.south = True
                self.west = True

    def __repr__(self) -> str:
        return self.char
    
def count_route_steps(x: int, y: int, island: list[list[PipePoint]], from_dir: str, steps: int) -> tuple[int, list[str]]:
    visited: list[str] = []
    while True:
        point = island[y][x]
        visited.append(f'{y:03d}{x:03d}')
        # print(f'[{x}, {y}]: "{point.char}" {from_dir} {steps} steps')
        if from_dir != 'north' and point.north and y - 1 >= 0:
            y = y - 1
            next_point = island[y][x]
            steps += 1
            next_point.dist = steps
            from_dir = 'south'
        elif from_dir != 'south' and point.south and y + 1 <= len(island):
            y = y + 1
            next_point = island[y][x]
            steps += 1
            next_point.dist = steps
            from_dir = 'north'
        elif from_dir != 'east' and point.east and x + 1 <= len(island[0]):
            x = x + 1
            next_point = island[y][x]
            steps += 1
            next_point.dist = steps
            from_dir = 'west'
        elif from_dir != 'west' and point.west and x - 1 >= 0:
            x = x - 1
            next_point = island[y][x]
            steps += 1
            next_point.dist = steps
            from_dir = 'east'
        else:
            return steps, visited 
        if next_point.start:
            return steps, visited
            
start_x = -1
start_y = -1
island: list[list[PipePoint]] = []
for y, line in enumerate(lines):
    point_list = []
    for x, point in enumerate(line):
        pipe_point = PipePoint(point)
        if pipe_point.start:
            start_x = x
            start_y = y
        point_list.append(pipe_point)
    island.append(point_list)

steps = 0
south_steps, south_visited = count_route_steps(start_x, start_y, island, 'south', 0)
west_steps, west_visisted = count_route_steps(start_x, start_y, island, 'west', 0)
max_steps = max(south_steps, west_steps)
print(max_steps)