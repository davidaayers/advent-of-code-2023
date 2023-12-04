import day1_funcs
import unittest

class TestDayOne(unittest.TestCase):

    def test_part1_transform_number(self):
        self.assertEqual(day1_funcs.part1_transform_number("1abc2"), 12)
        self.assertEqual(day1_funcs.part1_transform_number("pqr3stu8vwx"), 38)
        self.assertEqual(day1_funcs.part1_transform_number("a1b2c3d4e5f"), 15)
        self.assertEqual(day1_funcs.part1_transform_number("treb7uchet"), 77)


    def test_part2_transform_number(self):
        self.assertEqual(day1_funcs.part2_transform_number("two1nine"), 29)
        self.assertEqual(day1_funcs.part2_transform_number("eightwothree"), 83)
        self.assertEqual(day1_funcs.part2_transform_number("xtwone3four"), 24)
        self.assertEqual(day1_funcs.part2_transform_number("4nineeightseven2"), 42)
        self.assertEqual(day1_funcs.part2_transform_number("zoneight234"), 14)
        self.assertEqual(day1_funcs.part2_transform_number("7pqrstsixteen"), 76)
