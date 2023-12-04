import day4_funcs
import utils.util as util

input = util.read_file("input.txt")

scratch_cards = [day4_funcs.parse_scratch_card(line) for line in input]
part_1_answer = sum([card.score() for card in scratch_cards])
print(f"Part 1: {part_1_answer}")

# Part 2
part_2_answer = 0
print(f"Part 2: {part_2_answer}")