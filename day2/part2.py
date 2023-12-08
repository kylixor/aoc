from dataclasses import dataclass

file = open('day2/input.txt', 'r')
lines = file.read().splitlines()

@dataclass
class Drawing():
    red: int
    green: int
    blue: int

@dataclass
class Game():
    id: int
    drawings: list[Drawing]

    def max_red(self) -> int:
        return max(x.red for x in self.drawings)
    def max_green(self) -> int:
        return max(x.green for x in self.drawings)
    def max_blue(self) -> int:
        return max(x.blue for x in self.drawings)
    def power(self) -> int:
        return self.max_red() * self.max_green() * self.max_blue()
    
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
    power = game.power()
    sum += power
print(sum)