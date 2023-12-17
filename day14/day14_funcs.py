from utils.util import *


def parse_input(input_lines):
    width = len(input_lines[0])
    height = len(input_lines)
    platform = Platform(width, height)

    for y, line in enumerate(input_lines):
        for x, symbol in enumerate(line):
            if symbol == "O" or symbol == "#":
                platform.add_symbol(x, y, symbol)

    print(map_array_to_str(platform.platform_map))

    return platform


def calc_load_in_dir(platform, direction):
    total_load = 0
    if direction == NORTH:
        row_load = platform.height
        for line in platform.platform_map:
            num_rocks = [rock for rock in line if rock == "O"]
            total_load += len(num_rocks) * row_load
            row_load -= 1

    return total_load


class Platform:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.platform_map = [["." for x in range(width)] for y in range(height)]
        self.rocks = []

    def add_symbol(self, x, y, symbol):
        self.platform_map[y][x] = symbol
        if symbol == "O":
            self.rocks.append(Rock(x,y))

    def tilt(self, direction):
        dx = CARDINAL_DIRECTIONS[direction][1]
        dy = CARDINAL_DIRECTIONS[direction][0]

        for rock in self.rocks:
            can_move = True
            while can_move:
                new_x = rock.x + dx
                new_y = rock.y + dy
                test_symbol = self.platform_map[new_y][new_x]
                if (new_y > self.height or new_y < 0 or new_x > self.width or new_x < 0 or
                        test_symbol == "#" or test_symbol == "O"):
                    can_move = False
                else:
                    self.platform_map[new_y][new_x] = "O"
                    self.platform_map[rock.y][rock.x] = "."
                    rock.x = new_x
                    rock.y = new_y


class Rock:

    def __init__(self, x, y):
        self.x = x
        self.y = y
