from day14_funcs import *
import utils.util as util

input_lines = util.read_file("input.txt")

# Part 1
platform = parse_input(input_lines)
platform.tilt(NORTH)
part_1_answer = calc_load_on_north_pillar(platform)

print(f"Part 1: {part_1_answer}")

# Part 2
platform = parse_input(input_lines)
part_2_answer = calc_load_after_cycles(platform, 1_000_000_000)
print(f"Part 2: {part_2_answer}")
