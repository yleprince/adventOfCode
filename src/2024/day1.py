# 2024 Advent of Code day 1
from utils import get_input_lines


def prepare_input(lines):
    first_list = []
    second_list = []
    for line in lines:
        f, s = line.split("   ")
        first_list.append(int(f))
        second_list.append(int(s))
    return first_list, second_list


def puzzle1(lines):
    first_list, second_list = prepare_input(lines)
    first_list.sort()
    second_list.sort()

    distance = 0
    for left, right in zip(first_list, second_list):
        distance += abs(left - right)

    return distance


def puzzle2(lines):
    first_list, second_list = prepare_input(lines)

    similarity = 0

    # Values count on list 2
    values_count = {}
    for element in second_list:
        values_count[element] = values_count.get(element, 0) + 1

    for element in first_list:
        similarity += element * values_count.get(element, 0)

    return similarity


if __name__ == "__main__":
    dayNumber = 1

    example = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
    lines = get_input_lines(dayNumber)
    #    lines = example

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
