game_index = 0

file = open('day4/input.txt', 'r')
lines = file.read().splitlines()
total_games = len(lines)
copy_counter = {x: 1 for x in range(1, total_games + 1)}

for line in lines:
    game_index += 1
    game_str = line.split(':')[1].split('|')
    winners = [int(x.strip()) for x in game_str[0].strip().split(' ') if x]
    numbers = [int(x.strip()) for x in game_str[1].strip().split(' ') if x]
    points = 0
    for winner in winners:
        if winner in numbers:
            points += 1
    for index, card in enumerate(range(game_index + 1, game_index + points + 1)):
        copy_counter[game_index + index + 1] += 1 * copy_counter[game_index]
    print(f'Card {game_index}: {copy_counter[game_index]} copies')
print(sum(copy_counter.values()))