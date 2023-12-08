import day7_funcs
import unittest

test_input = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

# test input from reddit
# https://www.reddit.com/r/adventofcode/comments/18cr4xr/2023_day_7_better_example_input_not_a_spoiler/
# Helped me solve my problem!
test_input2 = """
2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41"""

test_input_lines = test_input.split("\n")
del test_input_lines[0]

hands = day7_funcs.parse_input(test_input_lines)


class TestDaySeven(unittest.TestCase):

    def test_parsing(self):
        self.assertEqual(hands[0].hand, "32T3K")
        self.assertEqual(hands[0].bid, 765)
        self.assertEqual(hands[0].rank, 6)
        self.assertEqual(hands[1].rank, 4)
        self.assertEqual(hands[2].rank, 5)
        self.assertEqual(hands[3].rank, 5)
        self.assertEqual(hands[4].rank, 4)

    def test_rank_hand(self):
        # Five of a kind
        self.assertEqual(day7_funcs.rank_hand("AAAAA"), 1)
        self.assertEqual(day7_funcs.rank_hand("22222"), 1)
        # four of a kind
        self.assertEqual(day7_funcs.rank_hand("AAAA2"), 2)
        self.assertEqual(day7_funcs.rank_hand("A2AAA"), 2)
        self.assertEqual(day7_funcs.rank_hand("2AAAA"), 2)
        self.assertEqual(day7_funcs.rank_hand("AAA2A"), 2)
        # full house
        self.assertEqual(day7_funcs.rank_hand("AAA22"), 3)
        self.assertEqual(day7_funcs.rank_hand("22AAA"), 3)
        self.assertEqual(day7_funcs.rank_hand("2A2A2"), 3)
        self.assertEqual(day7_funcs.rank_hand("22AA2"), 3)
        # three of a kind
        self.assertEqual(day7_funcs.rank_hand("22AK2"), 4)
        self.assertEqual(day7_funcs.rank_hand("222AK"), 4)
        self.assertEqual(day7_funcs.rank_hand("AK222"), 4)
        self.assertEqual(day7_funcs.rank_hand("2K322"), 4)
        # two pair
        self.assertEqual(day7_funcs.rank_hand("2332K"), 5)
        self.assertEqual(day7_funcs.rank_hand("K3322"), 5)
        self.assertEqual(day7_funcs.rank_hand("2K323"), 5)
        # one pair
        self.assertEqual(day7_funcs.rank_hand("2K343"), 6)
        self.assertEqual(day7_funcs.rank_hand("3K243"), 6)
        self.assertEqual(day7_funcs.rank_hand("KK243"), 6)
        self.assertEqual(day7_funcs.rank_hand("243KK"), 6)
        self.assertEqual(day7_funcs.rank_hand("K243K"), 6)
        # high card
        self.assertEqual(day7_funcs.rank_hand("23456"), 7)

    def test_hand_eq(self):
        hand1 = day7_funcs.Hand("23456", 1, day7_funcs.rank_hand("23456"))
        hand2 = day7_funcs.Hand("65432", 1, day7_funcs.rank_hand("23456"))
        self.assertTrue(hand1.__eq__(hand2))

    def test_calc_winnings(self):
        winnings = day7_funcs.calc_winnings(hands)
        self.assertEqual(winnings, 6440)

    def test_calc_winnings_with_jokers(self):
        joker_hands = day7_funcs.parse_input_with_jokers(test_input_lines)
        winnings = day7_funcs.calc_winnings(joker_hands)
        self.assertEqual(winnings, 5905)

    def test_calc_winnings_with_jokers2(self):
        test_input_lines2 = test_input2.split("\n")
        del test_input_lines2[0]

        hands2 = day7_funcs.parse_input_with_jokers(test_input_lines2)
        winnings = day7_funcs.calc_winnings(hands2)
        self.assertEqual(winnings, 6839)
