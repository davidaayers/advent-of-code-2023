from utils.util import *


def parse_input(input_lines):
    puzzle_map = parse_puzzle_map(input_lines)
    return ContraptionMap(puzzle_map)


def project_beam(contraption_map, initial_beam):
    beams = [initial_beam]
    splitters = []
    while beams:
        for beam in beams.copy():
            contraption_map.illuminate(beam.x, beam.y)
            next_x = beam.x + CARDINAL_DIRECTIONS[beam.direction][1]
            next_y = beam.y + CARDINAL_DIRECTIONS[beam.direction][0]

            # if this puts us off the map, end the beam
            if not contraption_map.puzzle_map.is_in_bounds(next_x, next_y):
                beams.remove(beam)
                continue

            beam.x = next_x
            beam.y = next_y

            check_symbol = contraption_map.puzzle_map.map_squares[next_y][next_x]

            if beam.direction == EAST:
                if check_symbol == "\\":
                    beam.direction = SOUTH
                elif check_symbol == "/":
                    beam.direction = NORTH
                elif check_symbol == "|" and not [next_x, next_y] in splitters:
                    beam.direction = SOUTH
                    new_beam = Beam(NORTH, next_x, next_y)
                    beams.append(new_beam)
                    splitters.append([next_x, next_y])
                elif [next_x, next_y] in splitters:
                    beams.remove(beam)
            elif beam.direction == WEST:
                if check_symbol == "\\":
                    beam.direction = NORTH
                elif check_symbol == "/":
                    beam.direction = SOUTH
                elif check_symbol == "|" and not [next_x, next_y] in splitters:
                    beam.direction = SOUTH
                    new_beam = Beam(NORTH, next_x, next_y)
                    beams.append(new_beam)
                    splitters.append([next_x, next_y])
                elif [next_x, next_y] in splitters:
                    beams.remove(beam)
            elif beam.direction == NORTH:
                if check_symbol == "\\":
                    beam.direction = WEST
                elif check_symbol == "/":
                    beam.direction = EAST
                elif check_symbol == "-" and not [next_x, next_y] in splitters:
                    beam.direction = EAST
                    new_beam = Beam(WEST, next_x, next_y)
                    beams.append(new_beam)
                    splitters.append([next_x, next_y])
                elif [next_x, next_y] in splitters:
                    beams.remove(beam)
            elif beam.direction == SOUTH:
                if check_symbol == "\\":
                    beam.direction = EAST
                elif check_symbol == "/":
                    beam.direction = WEST
                elif check_symbol == "-" and not [next_x, next_y] in splitters:
                    beam.direction = EAST
                    new_beam = Beam(WEST, next_x, next_y)
                    beams.append(new_beam)
                    splitters.append([next_x, next_y])
                elif [next_x, next_y] in splitters:
                    beams.remove(beam)


def find_best_beam(contraption_map):
    all_beams = []
    width = contraption_map.puzzle_map.width
    height = contraption_map.puzzle_map.height
    for x in range(width):
        beam_top = Beam(SOUTH, x, -1)
        contraption_map.light_map = PuzzleMap(width, height)
        project_beam(contraption_map, beam_top)
        all_beams.append(count_illuminated_squares(contraption_map))

        beam_bottom = Beam(NORTH, x, height)
        contraption_map.light_map = PuzzleMap(width, height)
        project_beam(contraption_map, beam_bottom)
        all_beams.append(count_illuminated_squares(contraption_map))

    for y in range(height):
        beam_left = Beam(EAST, -1, y)
        contraption_map.light_map = PuzzleMap(width, height)
        project_beam(contraption_map, beam_left)
        all_beams.append(count_illuminated_squares(contraption_map))

        beam_right = Beam(WEST, width, y)
        contraption_map.light_map = PuzzleMap(width, height)
        project_beam(contraption_map, beam_right)
        all_beams.append(count_illuminated_squares(contraption_map))

    all_beams.sort(reverse=True)
    return all_beams[0]


def count_illuminated_squares(contraption_map):
    illuminated = 0
    for line in contraption_map.light_map.map_squares:
        for c in line:
            if c == "#":
                illuminated += 1
    return illuminated


class ContraptionMap:

    def __init__(self, puzzle_map):
        self.puzzle_map = puzzle_map
        self.light_map = PuzzleMap(puzzle_map.width, puzzle_map.height)

    def illuminate(self, x, y):
        if self.light_map.is_in_bounds(x, y):
            self.light_map.map_squares[y][x] = "#"


class Beam:

    def __init__(self, initial_direction, x, y):
        self.direction = initial_direction
        self.x = x
        self.y = y

    def __str__(self):
        return f"{DIRECTION_NAMES[self.direction]}: {self.x}, {self.y}"
