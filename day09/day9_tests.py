import day9_funcs
import unittest

test_input = """
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

reading_histories = day9_funcs.parse_input(test_input_lines)


class TestDayNine(unittest.TestCase):

    def test_parsing(self):
        # check some random values
        self.assertEqual(reading_histories[0][0], 0)
        self.assertEqual(reading_histories[1][0], 1)
        self.assertEqual(reading_histories[2][0], 10)

    def test_calc_diffs_between_readings(self):
        diffs1 = day9_funcs.calc_diffs_between_readings(reading_histories[0])
        self.assertEqual(len(diffs1), 5)
        self.assertEqual(diffs1[0], 3)
        self.assertEqual(diffs1[1], 3)
        diffs2 = day9_funcs.calc_diffs_between_readings(reading_histories[1])
        self.assertEqual(len(diffs2), 5)
        self.assertEqual(diffs2[0], 2)
        self.assertEqual(diffs2[1], 3)
        self.assertEqual(diffs2[2], 4)
        self.assertEqual(diffs2[3], 5)
        self.assertEqual(diffs2[4], 6)

    def test_predict_next_reading(self):
        next_reading = day9_funcs.predict_next_reading(reading_histories[0])
        self.assertEqual(next_reading, 18)

        next_reading = day9_funcs.predict_next_reading(reading_histories[1])
        self.assertEqual(next_reading, 28)

        next_reading = day9_funcs.predict_next_reading(reading_histories[2])
        self.assertEqual(next_reading, 68)
