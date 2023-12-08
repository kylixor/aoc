from dataclasses import dataclass


MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14

file = open('day2/input.txt', 'r')
lines = file.read().splitlines()

@dataclass
class Drawing():
    red: int
    green: int
    blue: int

    def valid(self) -> bool:
        return True if self.red <= MAX_RED_CUBES and self.green <= MAX_GREEN_CUBES and self.blue <= MAX_BLUE_CUBES else False

@dataclass
class Game():
    id: int
    drawings: list[Drawing]

    def valid(self) -> bool:
        return all(x.valid() for x in self.drawings)
    
def parse_drawing(string: str) -> Drawing:
    drawing = Drawing(0, 0, 0)
    drawings_str = string.split(', ')
    for draw_str in drawings_str:
        cubes_str = draw_str.split(' ')
        if cubes_str[1] == 'red':
            drawing.red = int(cubes_str[0])
        if cubes_str[1] == 'green':
            drawing.green = int(cubes_str[0])
        if cubes_str[1] == 'blue':
            drawing.blue = int(cubes_str[0])
        # print(f'{cubes_str[0]} {cubes_str[1]}')
    return drawing

    
def parse_game(input_line: str) -> Game:
    game_str, drawings_list_str = input_line.split(': ', 1)
    drawings_list = drawings_list_str.split('; ')
    game_int = int(game_str.split(' ')[1])
    game = Game(game_int, [])
    for drawing_str in drawings_list:
        game.drawings.append(parse_drawing(drawing_str))
    return game


sum = 0
for line in lines:
    game = parse_game(line)
    if game.valid():
        print(f'Game {game.id}: Valid')
        sum += game.id
    else:
        print(f'Game {game.id}: Invalid')
print(sum)