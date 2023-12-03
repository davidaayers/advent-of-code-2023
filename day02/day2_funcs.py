import re


def parse_game(input_line):
    input_line_parts = input_line.split(":")
    game_num = int(re.sub(r"[a-zA-Z]", "", input_line_parts[0]))
    game = Game(game_num)

    rounds = input_line_parts[1].split(";")
    for r in rounds:
        draws = dict()
        draw_parts = r.split(",")

        for i in draw_parts:
            draw = i.strip().split(" ");
            draws[draw[1]] = int(draw[0])

        game.rounds.append(draws)

    return game


class Game:

    def __init__(self, game_num):
        self.game_num = game_num
        self.rounds = []

    def __str__(self):
        return f"Game: {self.game_num}, Rounds: {self.rounds}"

    def is_possible_with(self, red, green, blue):
        for r in self.rounds:
            if r.get('red', 0) > red or r.get('green', 0) > green or r.get('blue', 0) > blue:
                return False

        return True

    def power(self):
        red, green, blue = 0, 0, 0

        for r in self.rounds:
            r_red = r.get('red', 0)
            red = r_red if r_red > red else red
            r_blue = r.get('blue', 0)
            blue = r_blue if r_blue > blue else blue
            r_green = r.get('green', 0)
            green = r_green if r_green > green else green

        return red * green * blue
