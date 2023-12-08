import day8_funcs
import utils.util as util

input = util.read_file("input.txt")

desert_map = day8_funcs.parse_input(input)

part_1_answer = day8_funcs.walk_map(desert_map)
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")