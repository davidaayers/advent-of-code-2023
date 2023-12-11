import day11_funcs
import utils.util as util

input_lines = util.read_file("input.txt")

galaxy_map = day11_funcs.parse_input(input_lines)

part_1_answer = day11_funcs.calc_distances(galaxy_map, 1)
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = day11_funcs.calc_distances(galaxy_map, 1000000-1)
print(f"Part 2: {part_2_answer}")