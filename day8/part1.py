from itertools import cycle


file = open('day8/input.txt', 'r')
lines = file.read().splitlines()

START = 'AAA'
END = 'ZZZ'
points: dict[str, tuple[str, str]] = {}
instructions = ''

for idx, line in enumerate(lines):
    if idx > 1:
        split_line = line.split(' = ')
        code = split_line[0]
        left_right = split_line[1].split(', ')
        left = left_right[0].lstrip('(')
        right = left_right[1].rstrip(')')
        points[code] = (left, right)
    elif idx == 0:
        instructions = line


steps = 0
current = START
for direction in cycle(instructions):
    if direction == 'L':
        current = points[current][0]
    elif direction == 'R':
        current = points[current][1]
    steps += 1
    if current == END:
        break

print(steps)