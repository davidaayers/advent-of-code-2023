from day17_funcs import *
import unittest

test_input = r"""
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDaySeventeen(unittest.TestCase):

    def test_parsing(self):
        island_map = parse_input(test_input_lines)
        print(island_map)

    def test_find_path(self):
        island_map = parse_input(test_input_lines)
        find_path(island_map)

