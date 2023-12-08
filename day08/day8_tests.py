import day8_funcs
import unittest

test_input = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

test_input2 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

test_input_lines2 = test_input2.split("\n")
del test_input_lines2[0]


class TestDayEight(unittest.TestCase):

    def test_parsing(self):
        desert_map = day8_funcs.parse_input(test_input_lines)
        self.assertEqual(desert_map[0], "RL")

    def test_walk_map(self):
        desert_map = day8_funcs.parse_input(test_input_lines)
        steps = day8_funcs.walk_map(desert_map)
        self.assertEqual(steps, 2)

        desert_map2 = day8_funcs.parse_input(test_input_lines2)
        steps2 = day8_funcs.walk_map(desert_map2)
        self.assertEqual(steps2, 6)

