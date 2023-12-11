race_time = 47_847_467
record_distance = 207_139_412_091_014

winning_methods = 0
for time in range(0, race_time):
    accel = time
    distance = accel * (race_time - time)

    record = record_distance
    if distance > record:
        winning_methods += 1
print(f'You can win {winning_methods} different methods!')