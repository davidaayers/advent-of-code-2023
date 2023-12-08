import day7_funcs
import utils.util as util

input = util.read_file("input.txt")

hands = day7_funcs.parse_input(input)

part_1_answer = day7_funcs.calc_winnings(hands)
print(f"Part 1: {part_1_answer}")

# Part 2
joker_hands = day7_funcs.parse_input_with_jokers(input)
part_2_answer = day7_funcs.calc_winnings(joker_hands)
print(f"Part 2: {part_2_answer}")