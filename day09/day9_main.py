import day9_funcs
import utils.util as util

input = util.read_file("input.txt")

readings = day9_funcs.parse_input(input)
next_readings = [day9_funcs.predict_next_reading(reading) for reading in readings]

part_1_answer = sum(next_readings)
print(f"Part 1: {part_1_answer}")

# Part 2
prev_readings = [day9_funcs.predict_previous_reading(reading) for reading in readings]
part_2_answer = sum(prev_readings)
print(f"Part 2: {part_2_answer}")