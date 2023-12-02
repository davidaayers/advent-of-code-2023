import part1
import utils.util as util

input = util.read_file("input.txt")
numbers = part1.transform_numbers(input)
part_1_answer = part1.sum_numbers(numbers)
print(part_1_answer)