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


def calc_load_on_north_pillar(platform):
    total_load = 0
    row_load = platform.height
    for line in platform.platform_map:
        num_rocks = [rock for rock in line if rock == "O"]
        total_load += len(num_rocks) * row_load
        row_load -= 1

    return total_load


def calc_load_after_cycles(platform, cycles):
    load_after_cycle = 0
    for c in range(cycles):
        for direction in DIRS:
            platform.tilt(direction)

    return load_after_cycle


class Platform:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.platform_map = [["." for x in range(width)] for y in range(height)]
        self.rocks = []

    def add_symbol(self, x, y, symbol):
        self.platform_map[y][x] = symbol
        if symbol == "O":
            self.rocks.append(Rock(x, y))

    def tilt(self, direction):

        print(f"Tilting {DIRECTION_NAMES[direction]}")

        dx = CARDINAL_DIRECTIONS[direction][1]
        dy = CARDINAL_DIRECTIONS[direction][0]

        # Sort our list of rocks based on the direction we're
        rocks = self.rocks.copy()

        # no sorting necessary for NORTH, it's the way they are sorted
        # initially
        if direction == WEST:
            def w_sort(sr):
                return sr.x, sr.y

            rocks.sort(key=w_sort)

        if direction == EAST:
            def e_sort(sr):
                return -sr.x, sr.y

            rocks.sort(key=e_sort)

        if direction == SOUTH:
            def s_sort(sr):
                return -sr.y, sr.x

            rocks.sort(key=s_sort)

        if direction == NORTH:
            def s_sort(sr):
                return sr.y, sr.x

            rocks.sort(key=s_sort)

        for rock in rocks:
            can_move = True
            while can_move:
                new_x = rock.x + dx
                new_y = rock.y + dy
                if new_y > self.height - 1 or new_y < 0 or new_x > self.width - 1 or new_x < 0:
                    break

                test_symbol = self.platform_map[new_y][new_x]
                if test_symbol == "#" or test_symbol == "O":
                    break
                else:
                    self.platform_map[new_y][new_x] = "O"
                    self.platform_map[rock.y][rock.x] = "."
                    rock.x = new_x
                    rock.y = new_y

        print(map_array_to_str(self.platform_map))


class Rock:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Rock ({self.x},{self.y})"

    def __repr__(self):
        return self.__str__()
