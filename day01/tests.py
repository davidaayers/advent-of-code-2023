import part1
import unittest

class TestDayOne(unittest.TestCase):

    def test_transform_number(self):
        self.assertEqual(part1.transform_number("12"),12)
        self.assertEqual(part1.transform_number("12345"),15)
        self.assertEqual(part1.transform_number("7"), 77)

    def test_transform_numbers(self):
        input = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
        expected = [12,38,15,77]
        self.assertEqual(part1.transform_numbers(input),expected)

