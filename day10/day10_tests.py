import day10_funcs
import unittest

test_input = """
-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

test_input2 = """
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

reading_histories = day9_funcs.parse_input(test_input_lines)


class TestDayTen(unittest.TestCase):

    def test_parsing(self):
