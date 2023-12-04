# Description Advent of Code day 4

from utils.utils import get_input_lines


def parse_cards_from_input(lines):
    cards = []
    for line in lines:
        win_raw, have_raw = line.split(" | ")
        win = {int(x) for x in win_raw.split(": ")[1].split(" ") if x != ""}
        have = {int(x) for x in have_raw.split(" ") if x != ""}
        cards.append((win, have))
    return cards


def puzzle1(lines):
    cards = parse_cards_from_input(lines)

    points = 0
    for card in cards:
        win, have = card
        nb_matches = len(win.intersection(have))
        score = 0 if nb_matches == 0 else 2 ** (nb_matches - 1)
        points += score
    return points


def puzzle2(lines):
    cards = parse_cards_from_input(lines)

    cards_occurences = {i: 1 for i in range(len(cards))}

    for i, card in enumerate(cards):
        win, have = card
        nb_matches = len(win.intersection(have))
        for j in range(i + 1, i + 1 + nb_matches):
            cards_occurences[j] = cards_occurences.get(j, 0) + cards_occurences[i]
    return sum(cards_occurences.values())


if __name__ == "__main__":
    dayNumber = 4

    example = [
        "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
        "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
        "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
        "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
        "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
        "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
    ]

    lines = get_input_lines(dayNumber)

    # Puzzle 1
    first_example = puzzle1(example)
    print("Example 1: " + str(first_example))

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))
    print()

    # Puzzle 2
    second_example = puzzle2(example)
    print("Example 2: " + str(second_example))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
