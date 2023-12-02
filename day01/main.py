import day1_funcs
import utils.util as util

input = util.read_file("input.txt")

# Part 1
part_1_answer = sum([day1_funcs.part1_transform_number(n) for n in input])
print(part_1_answer)

# Part 2
