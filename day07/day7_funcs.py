card_values = "AKQJT98765432"
card_values_with_jokers = "AKQT98765432J"


def parse_input(input_lines):
    hands = []
    for line in input_lines:
        parts = line.split()
        hands.append(Hand(parts[0], int(parts[1]), rank_hand(parts[0])))

    return hands


def parse_input_with_jokers(input_lines):
    hands = []
    for line in input_lines:
        parts = line.split()
        hands.append(Hand(parts[0], int(parts[1]), rank_hand_with_jokers(parts[0]), True))

    return hands


def rank_hand_with_jokers(hand):
    if "J" not in hand:
        return rank_hand(hand)

    # we need to try to substitute J for all the other cards, and pick
    # the best possible hand as a result
    lowest_rank = 7
    cards = build_card_dict(hand)
    for card in cards.keys():
        test_hand = hand.replace("J", card)
        test_rank = rank_hand(test_hand)
        if test_rank < lowest_rank:
            lowest_rank = test_rank

    return lowest_rank


def build_card_dict(hand):
    cards = dict()
    for card in sorted(hand):
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    return cards


def rank_hand(hand):
    cards = build_card_dict(hand)
    keys = list(cards.keys())

    # five of a kind
    if len(cards) == 1:
        return 1

    # four of a kind
    if len(cards) == 2 and (cards[keys[0]] == 4 or cards[keys[1]] == 4):
        return 2

    # full house
    if len(cards) == 2 and ((cards[keys[0]] == 3 and cards[keys[1]] == 2) or
                            (cards[keys[0]] == 2 and cards[keys[1]] == 3)):
        return 3

    # three of a kind
    if len(cards) == 3 and (cards[keys[0]] == 3 or cards[keys[1]] == 3 or cards[keys[2]] == 3):
        return 4

    # two pair
    if len(cards) == 3 and len({c: cnt for c, cnt in cards.items() if cnt == 2}) == 2:
        return 5

    # one pair
    if len(cards) == 4 and len({c: cnt for c, cnt in cards.items() if cnt == 2}) == 1:
        return 6

    return 7


def calc_winnings(hands):
    hands_sorted = sorted(hands)
    hands_sorted.reverse()
    winnings = 0
    for idx, hand in enumerate(hands_sorted):
        rank = idx + 1
        winnings += rank * hand.bid

    return winnings


class Hand:

    def __init__(self, hand, bid, rank, use_jokers=False):
        self.hand = hand
        self.bid = bid
        self.rank = rank
        self.use_jokers = use_jokers

    def __str__(self):
        return f"Hand = {self.hand}, Bid={self.bid}, Rank = {self.rank}"

    def __eq__(self, other):
        return sorted(self.hand) == sorted(other.hand)

    def __lt__(self, other):
        if other.rank > self.rank:
            return True

        if other.rank < self.rank:
            return False

        # same rank, compare first card (then 2nd, etc.)
        for i in range(5):
            values = card_values_with_jokers if self.use_jokers else card_values
            my_card = values.index(self.hand[i])
            other_card = values.index(other.hand[i])
            if my_card < other_card:
                return True

            if my_card > other_card:
                return False
