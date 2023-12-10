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

test_input_lines2 = test_input2.split("\n")
del test_input_lines2[0]

pipe_map = day10_funcs.parse_input(test_input_lines)
pipe_map2 = day10_funcs.parse_input(test_input_lines2)


class TestDayTen(unittest.TestCase):

    def test_parsing(self):
        print(pipe_map)
        self.assertEqual(len(pipe_map.loop_nodes), 8)
        self.assertEqual(len(pipe_map2.loop_nodes), 16)

