def parse_scratch_card(input_line):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    input_line_parts = input_line.split(":")
    card_number = ' '.join(input_line_parts[0].split()).split(" ")[1]
    number_parts = input_line_parts[1].split("|")
    winning_nums_str = number_parts[0].strip().split(" ")
    winning_nums_str = [str for str in winning_nums_str if str != '']
    winning_nums = [int(s) for s in winning_nums_str]
    present_nums_str = number_parts[1].strip().split(" ")
    present_nums_str = [str for str in present_nums_str if str != '']

    present_nums = [int(s) for s in present_nums_str]
    return ScratchCard(int(card_number), winning_nums, present_nums)


def process_cards(scratch_cards):
    working_cards = scratch_cards.copy()
    final_cards = list()

    while working_cards:
        # grab the first one
        card = working_cards.pop(0)
        # print(f"Processing card: {card}")
        final_cards.append(card)
        # now, add cards for any winners on this card
        if card.num_winners == 0:
            continue

        for i in range(card.card_number, card.card_number + card.num_winners()):
            working_cards.append(scratch_cards[i])

    return final_cards


class ScratchCard:

    def __init__(self, card_number, winning_numbers, present_numbers):
        self.card_number = card_number
        self.winning_numbers = winning_numbers
        self.present_numbers = present_numbers

    def num_winners(self):
        return len(list(set(self.winning_numbers) & set(self.present_numbers)))

    def score(self):
        num_winners = self.num_winners()

        if num_winners == 0:
            return 0

        score = 1
        for i in range(num_winners - 1):
            score *= 2

        return score

    def __str__(self):
        return f"Card {self.card_number} winners: {self.num_winners()} score: {self.score()}"
