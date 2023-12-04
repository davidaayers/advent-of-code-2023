import day2_funcs
import utils.util as util

input = util.read_file("input.txt")

games = [day2_funcs.parse_game(n) for n in input]
playable_games = [game for game in games if game.is_possible_with(12, 13, 14)]
part_1_answer = sum(game.game_num for game in playable_games)
print(f"Part 1: {part_1_answer}")


# Part 2
part_2_answer = sum(game.power() for game in games)
print(f"Part 2: {part_2_answer}")