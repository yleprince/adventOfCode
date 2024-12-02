# Description Advent of Code day 3

import re

from utils.utils import get_input_lines


def is_special_char(char):
    return re.search(r"\d|\.", char) is None


def is_digit(char):
    return re.search(r"\d", char) is not None


def get_special_char_coordinates(lines):
    coordinates = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if is_special_char(lines[i][j]):
                coordinates.append((i, j))
    return coordinates


def get_adjacent_digits_coordinates(lines, coordinates):
    adjacent_digits_coordinates = set()
    for i in range(max(coordinates[0] - 1, 0), min(coordinates[0] + 2, len(lines[0]))):
        for j in range(max(coordinates[1] - 1, 0), min(coordinates[1] + 2, len(lines))):
            if is_digit(lines[i][j]):
                adjacent_digits_coordinates.add((i, j))
    return adjacent_digits_coordinates


def search_full_digit(lines, coordinates):
    i, j = coordinates
    digit_str = lines[i][j]

    # search left
    while j > 0 and is_digit(lines[i][j - 1]):
        j -= 1
        digit_str = lines[i][j] + digit_str

    # search right
    i, j = coordinates
    while j < len(lines[0]) - 1 and is_digit(lines[i][j + 1]):
        j += 1
        digit_str += lines[i][j]

    # we also return the coordinates of the number rightmost digit
    # this hack prevents us from searching the same number twice
    return (int(digit_str), (i, j))


def puzzle1(lines):
    special_char_coordinates = get_special_char_coordinates(lines)

    adjacent_digits_coordinates = set()
    for coordinates in special_char_coordinates:
        adjacent_digits_coordinates.update(
            get_adjacent_digits_coordinates(lines, coordinates)
        )

    digits = set()
    for coordinates in adjacent_digits_coordinates:
        digits.add(search_full_digit(lines, coordinates))

    sum_digits = sum(digit for digit, _ in digits)

    return sum_digits


# ---------------------------- Puzzle 2 ----------------------------


def get_stars_coordinates(lines):
    coordinates = []
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "*":
                coordinates.append((i, j))
    return coordinates


def puzzle2(lines):
    stars_coordinates = get_stars_coordinates(lines)

    result = 0
    for coordinates in stars_coordinates:
        adjacent_digits = set()
        for adjacent_digits_coordinates in get_adjacent_digits_coordinates(
            lines, coordinates
        ):
            adjacent_digits.add(search_full_digit(lines, adjacent_digits_coordinates))
        if len(adjacent_digits) == 2:
            result += adjacent_digits.pop()[0] * adjacent_digits.pop()[0]

    return result


if __name__ == "__main__":
    dayNumber = 3

    example = [
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    ]

    lines = get_input_lines(dayNumber)

    # Puzzle 1
    first_example = puzzle1(example)
    print("Example 1: " + str(first_example))

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    print("")
    # Puzzle 2
    second_example = puzzle2(example)
    print("Example 2: " + str(second_example))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
