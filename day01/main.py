import day1_funcs
import utils.util as util

input = util.read_file("input.txt")

# Part 1
part_1_answer = sum([day1_funcs.part1_transform_number(n) for n in input])
print(f"Part 1: {part_1_answer}")


# Part 2
part_2_answer = sum([day1_funcs.part2_transform_number(n) for n in input])
print(f"Part 2: {part_2_answer}")
