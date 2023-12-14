from day13_funcs import *
import unittest

test_input = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]


class TestDayTwelve(unittest.TestCase):

    def test_parsing(self):
        print("test)")

