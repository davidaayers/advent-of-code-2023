import day4_funcs
import unittest

test_input = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

class TestDayFour(unittest.TestCase):

    def test_score(self):
        scratch_cards = [day4_funcs.parse_scratch_card(line) for line in test_input_lines]
        self.assertEqual(scratch_cards[0].score(), 8)
        self.assertEqual(scratch_cards[1].score(), 2)
        self.assertEqual(scratch_cards[2].score(), 2)
        self.assertEqual(scratch_cards[3].score(), 1)
        self.assertEqual(scratch_cards[4].score(), 0)
        self.assertEqual(scratch_cards[5].score(), 0)

    def test_process_cards(self):
        scratch_cards = [day4_funcs.parse_scratch_card(line) for line in test_input_lines]
        final_cards = day4_funcs.process_cards(scratch_cards)
        self.assertEqual(len(final_cards), 30)