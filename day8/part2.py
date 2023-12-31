from itertools import cycle
import math


file = open('day8/input.txt', 'r')
lines = file.read().splitlines()

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

start_points = [x for x in points if x.endswith('A')]

def calc_cycle_distance(start: str) -> int:
    steps = 0
    current = start
    for direction in cycle(instructions):
        if direction == 'L':
            current = points[current][0]
        elif direction == 'R':
            current = points[current][1]
        steps += 1
        if current.endswith('Z'):
            break
    return steps

point_tracker: dict[str, tuple[str, int]] = {x:(x, calc_cycle_distance(x)) for x in start_points}

# steps = 0
# for direction in cycle(instructions):
#     if direction == 'L':
#         for start_point in start_points:
#             point_tracker[start_point] = points[point_tracker[start_point]][0]
#     elif direction == 'R':
#         for start_point in start_points:
#             point_tracker[start_point] = points[point_tracker[start_point]][1]
#     steps += 1
#     if steps % 100000 == 0:
#         print(steps)
#     if all(point_tracker[x].endswith('Z') for x in point_tracker):
#         break

print(point_tracker)
print(math.lcm(*[point_tracker[x][1] for x in point_tracker]))