# 2024 Advent of Code day 2
from utils import get_input_lines


def prepare_input(lines):
    return [[int(value) for value in line.split(" ")] for line in lines]


def is_report_safe(report):
    safe = True
    derivative = []
    for i in range(len(report) - 1):
        derivative.append(report[i + 1] > report[i])
        diff = abs(report[i + 1] - report[i])
        if diff < 1 or diff > 3:
            safe = False
            break

    return safe and len(set(derivative)) == 1


def puzzle1(lines):
    reports = prepare_input(lines)
    counter = 0
    for report in reports:
        if is_report_safe(report):
            counter += 1
    return counter


def puzzle2(lines):
    reports = prepare_input(lines)
    counter = 0
    for report in reports:
        if is_report_safe(report):
            counter += 1
        else:
            for i in range(len(report)):
                new_report = report[:i] + report[i + 1 :]
                if is_report_safe(new_report):
                    counter += 1
                    break
    return counter


if __name__ == "__main__":
    dayNumber = 2

    example = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    lines = get_input_lines(dayNumber)
    # lines = example

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
