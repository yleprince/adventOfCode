# Description Advent of Code day 1

import re

import requests

from constants import COOKIES, DIGITS_STR


def get_input_lines(dayNumber):
    url = "https://adventofcode.com/2023/day/" + str(dayNumber) + "/input"
    r = requests.get(url, cookies=COOKIES)
    return r.text.splitlines()


def extract_digits1(line):
    return re.findall(r"\d", line)


def puzzle1(lines):
    counter = 0
    for line in lines:
        digits = extract_digits1(line)
        counter += int(digits[0]) * 10
        counter += int(digits[-1])
    return counter


def digit_str_to_int(digit_str):
    if digit_str in DIGITS_STR:
        return DIGITS_STR.index(digit_str)
    else:
        return int(digit_str)


def extract_digits2(line):
    extracted_digits = re.findall(f"(?=(\d|{'|'.join(DIGITS_STR)}))", line)
    useful_digits = [extracted_digits[0], extracted_digits[-1]]
    return [digit_str_to_int(d) for d in useful_digits]


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
