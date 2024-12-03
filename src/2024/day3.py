# 2024 Advent of Code day 3
import re

from utils import get_input_lines


def process_line(line):
    lines = line.split("mul(")
    result = 0
    for l in lines:
        if ")" in l:
            inside = l.split(")")[0]
            digits = re.findall(r"\d+", inside)
            if len(digits) == 2 and inside == ",".join(digits):
                result += int(digits[0]) * int(digits[1])
    return result


def puzzle1(lines):
    result = 0
    for line in lines:
        result += process_line(line)
    return result


def puzzle2(lines):
    line = "".join(lines)
    tokens = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)

    result = 0
    should_mult = True
    for token in tokens:
        if token == "do()":
            should_mult = True
        elif token == "don't()":
            should_mult = False
        else:
            if should_mult:
                digits = re.findall(r"\d+", token)
                result += int(digits[0]) * int(digits[1])
    return result


if __name__ == "__main__":
    dayNumber = 3

    example = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    lines = get_input_lines(dayNumber)
    # lines = [example]

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    example2 = (
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    )
    # lines = [example2]

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
