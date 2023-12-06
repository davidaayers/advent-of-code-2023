def parse_input(input_lines):
    # Time:      7  15   30
    # Distance:  9  40  200
    times = [int(time) for time in input_lines[0].split(":")[1].split()]
    distances = [int(time) for time in input_lines[1].split(":")[1].split()]

    races = []
    for idx, time in enumerate(times):
        races.append([time, distances[idx]])

    return races


def find_num_ways_to_win(race):
    num_ways_to_win = 0
    record_distance = race[1]
    for speed in range(race[0]):
        time_left_to_race = race[0] - speed
        distance = speed * time_left_to_race
        winner = distance > record_distance
        if winner:
            num_ways_to_win += 1

    return num_ways_to_win
