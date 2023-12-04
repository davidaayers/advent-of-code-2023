import day2_funcs
import unittest

lines = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]


class TestDayTwo(unittest.TestCase):

    def test_parse_games(self):
        game1 = day2_funcs.parse_game(lines[0])
        self.assertEqual(game1.game_num, 1)
        self.assertEqual(len(game1.rounds), 3)
        game2 = day2_funcs.parse_game(lines[1])
        self.assertEqual(game2.game_num, 2)
        self.assertEqual(len(game2.rounds), 3)
        game3 = day2_funcs.parse_game(lines[2])
        self.assertEqual(game3.game_num, 3)
        self.assertEqual(len(game3.rounds), 3)
        game4 = day2_funcs.parse_game(lines[3])
        self.assertEqual(game4.game_num, 4)
        self.assertEqual(len(game4.rounds), 3)
        game5 = day2_funcs.parse_game(lines[4])
        self.assertEqual(game5.game_num, 5)
        self.assertEqual(len(game5.rounds), 2)

    def test_is_possible(self):
        game1 = day2_funcs.parse_game(lines[0])
        self.assertTrue(game1.is_possible_with(12, 13, 14))
        self.assertEqual(game1.power(), 48)
        game2 = day2_funcs.parse_game(lines[1])
        self.assertTrue(game2.is_possible_with(12, 13, 14))
        self.assertEqual(game2.power(), 12)
        game3 = day2_funcs.parse_game(lines[2])
        self.assertFalse(game3.is_possible_with(12, 13, 14))
        self.assertEqual(game3.power(), 1560)
        game4 = day2_funcs.parse_game(lines[3])
        self.assertFalse(game4.is_possible_with(12, 13, 14))
        self.assertEqual(game4.power(), 630)
        game5 = day2_funcs.parse_game(lines[4])
        self.assertTrue(game5.is_possible_with(12, 13, 14))
        self.assertEqual(game5.power(), 36)
