def parse_input(input_lines):
    reading_histories = []
    for line in input_lines:
        parts = line.split()
        reading_histories.append([int(part) for part in parts])
    return reading_histories


def predict_next_reading(reading_history):
    all_diffs = calc_diffs(reading_history)
    all_diffs.reverse()
    next_reading = 0

    for idx, diff in enumerate(all_diffs):
        if idx == 0:
            continue

        next_reading = next_reading + diff[-1]

    return reading_history[-1] + next_reading


def predict_previous_reading(reading_history):
    all_diffs = calc_diffs(reading_history)
    all_diffs.reverse()
    next_reading = 0

    for idx, diff in enumerate(all_diffs):
        if idx == 0:
            continue

        next_reading = diff[0] - next_reading

    return reading_history[0] - next_reading


def calc_diffs(reading_history):
    next_diffs = reading_history
    all_diffs = []

    while True:
        diffs = calc_diffs_between_readings(next_diffs)
        all_diffs.append(diffs)

        # if they are all zeros, bail
        if len([r for r in diffs if r == 0]) == len(diffs):
            break

        next_diffs = diffs

    return all_diffs


def calc_diffs_between_readings(reading_history):
    last = reading_history[0]
    diffs = []
    for idx in range(1, len(reading_history)):
        diffs.append(reading_history[idx] - last)
        last = reading_history[idx]
    return diffs
