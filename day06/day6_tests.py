import day6_funcs
import unittest

test_input = """
Time:      7  15   30
Distance:  9  40  200"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

races = day6_funcs.parse_input(test_input_lines)

class TestDaySix(unittest.TestCase):

    def test_parsing(self):
        self.assertEqual(races[0][0], 7)
        self.assertEqual(races[0][1], 9)

    def test_find_num_ways_to_win(self):
        self.assertEqual(day6_funcs.find_num_ways_to_win(races[0]), 4)
        self.assertEqual(day6_funcs.find_num_ways_to_win(races[1]), 8)
        self.assertEqual(day6_funcs.find_num_ways_to_win(races[2]), 9)
