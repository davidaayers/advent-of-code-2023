from day14_funcs import *
import utils.util as util

input_lines = util.read_file("input.txt")

# Part 1
platform = parse_input(input_lines)
platform.tilt(NORTH)
part_1_answer = calc_load_in_dir(platform, NORTH)

print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")