from ast import Num
from dataclasses import dataclass


file = open('day3/input.txt', 'r')
lines = file.read().splitlines()

width = len(lines[0])
height = len(lines)

engine: list[list[str]] = [['.' for _ in range(height)] for _ in range(width)]

sum = 0
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != '.':
            engine[i][j] = char

@dataclass
class Number:
    start_x: int
    start_y: int
    num: int
    
    def __hash__(self) -> int:
        return hash(f'{self.start_x} {self.start_y}')

def find_rest_of_number(start_y: int, start_x: int) -> Number:
    found_digit = engine[start_y][start_x]
    x = start_x
    while x > 0 and engine[start_y][x - 1].isdigit():
        x -= 1
        found_digit = engine[start_y][x] + found_digit
    left_x = x
    x = start_x
    while x < height - 1 and engine[start_y][x + 1].isdigit():
        x += 1
        found_digit = found_digit + engine[start_y][x]
    return Number(left_x, start_y, int(found_digit))

def search_adjacent(y: int, x: int) -> set[Number]:
    surrounding_nums = set()
    min_yval = max(0, y - 1)
    max_yval = min(height - 1, y + 1)
    min_xval = max(0, x - 1)
    max_xval = min(width - 1, x + 1)
    for y in range(min_yval, max_yval + 1):
        for x in range(min_xval, max_xval + 1):
            char = engine[y][x]
            if char.isdigit():
                num = find_rest_of_number(y, x)
                surrounding_nums.add(num)
    return surrounding_nums
                

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == '*':
            nums = search_adjacent(y, x)
            if len(nums) == 2:
                nums_list = list(nums)
                sum += nums_list[0].num * nums_list[1].num
print(sum)