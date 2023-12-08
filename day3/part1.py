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

for i, line in enumerate(lines):
    end_j = 0
    for j, char in enumerate(line):
        if j < end_j:
            continue
        print(f'Starting search at [{i}, {j}]')
        if char.isdigit():
            end_j = j
            while end_j < height - 1 and engine[i][end_j + 1].isdigit():
                end_j += 1
            number = int(''.join([engine[i][z] for z in range(j, min(height - 1, end_j + 1))]))
            print(f'Number ({number}) found at [{i}, {j}:{min(height - 1, end_j)}]')
            min_yval = max(0, i - 1)
            max_yval = min(height - 1, i + 1)
            for y in range(min_yval, max_yval + 1):
                min_xval = max(0, j - 1)
                max_xval = min(width - 1, end_j + 1)
                for x in range(min_xval, max_xval + 1):
                    test_char = engine[y][x]
                    print(f'Checking [{y}, {x}]')
                    if not test_char.isalnum() and test_char != '.':
                        number = int(''.join([engine[i][z] for z in range(j, end_j + 1)]))
                        print(f'  Found symbol next to number {number} at [{y}, {x}]')
                        sum += number
            end_j += 2
print(sum)