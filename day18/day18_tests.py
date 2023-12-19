from day18_funcs import *
import unittest

test_input = r"""
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayEighteen(unittest.TestCase):

    def test_parsing(self):
        instructions = parse_input(test_input_lines)
        self.assertEqual(EAST, instructions[0][0])
        self.assertEqual(6, instructions[0][1])
        self.assertEqual("70c710", instructions[0][2])

    def test_dig_edge(self):
        instructions = parse_input(test_input_lines)
        dig_map = dig_edge(instructions, 7, 10, 0 , 0)
        print(dig_map)
        flood_fill_map(dig_map, 0, 0)
        squares = count_squares(dig_map)
        print(dig_map)
        print(squares)
