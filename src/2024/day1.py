# 2024 Advent of Code day 1
import requests


def get_input_lines(dayNumber):
    url = "https://adventofcode.com/2024/day/" + str(dayNumber) + "/input"
    r = requests.get(url, cookies=COOKIES)
    return r.text.splitlines()

def puzzle1(lines):
    counter = 0
    for line in lines:
        digits = extract_digits1(line)
        counter += int(digits[0]) * 10
        counter += int(digits[-1])
    return counter


def puzzle2(lines):
    counter = 0
    for line in lines:
        digits = extract_digits2(line)
        counter += int(digits[0]) * 10
        counter += int(digits[-1])
    return counter


if __name__ == "__main__":
    dayNumber = 1

    lines = get_input_lines(dayNumber)
    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
