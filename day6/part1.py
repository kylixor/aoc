file = open('day6/input.txt', 'r')
lines = file.read().splitlines()
times = list(map(int, lines[0].split(':')[1].split()))
distances = list(map(int, lines[1].split(':')[1].split()))

sum = 1
for idx, race_time in enumerate(times):
    winning_methods = 0
    print(f'Race {idx + 1}:')
    for time in range(0, race_time):
        accel = time
        distance = accel * (race_time - time)

        record = distances[idx]
        if distance > record:
            winning_methods += 1
    print(f'You can win {winning_methods} different methods!')
    sum *= winning_methods
print(sum)