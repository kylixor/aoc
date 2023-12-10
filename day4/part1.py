sum = 0
game_index = 0
for line in open('day4/input.txt', 'r').read().splitlines():
    game_index += 1
    game_str = line.split(':')[1].split('|')
    winners = [int(x.strip()) for x in game_str[0].strip().split(' ') if x]
    numbers = [int(x.strip()) for x in game_str[1].strip().split(' ') if x]
    points = 0
    for winner in winners:
        if winner in numbers:
            if points == 0:
                points += 1
            else:
                points *= 2
    sum += points
    print(f'Game {game_index}: {points} points')
print(sum)