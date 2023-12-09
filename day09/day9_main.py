import day9_funcs
import utils.util as util

input = util.read_file("input.txt")

readings = day9_funcs.parse_input(input)
next_readings = [day9_funcs.predict_next_reading(reading) for reading in readings]

part_1_answer = sum(next_readings)
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")