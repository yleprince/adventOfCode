# Description Advent of Code day 6

from utils.utils import get_input_lines

# from functools import lru_cache


def parse_input(lines):
    def get_digit(line):
        print(line)
        return [int(d) for d in line.split(": ")[1].split(" ") if d != ""]

    times = get_digit(lines[0])
    distances = get_digit(lines[1])
    inputs = [(t, d) for t, d in zip(times, distances)]
    return inputs


# @lru_cache(maxsize=None)
def get_distance(press_time, race_time):
    return (race_time - press_time) * press_time


def get_possibilities(time, distance):
    possibility = []
    for press_time in range(0, time):
        possibility.append(get_distance(press_time, time))
    return len([p for p in possibility if p > distance])


def puzzle1(lines):
    inputs = parse_input(lines)
    nb_ways = 1
    for time, distance in inputs:
        nb_ways *= get_possibilities(time, distance)
    return nb_ways


# ------------------------------
# Puzzle 2
# ------------------------------


def parse_input2(lines):
    def get_digit(line):
        line_ = line.replace(" ", "")
        return int(line_.split(":")[1])

    return get_digit(lines[0]), get_digit(lines[1])


def puzzle2(lines):
    time, distance = parse_input2(lines)
    return get_possibilities(time, distance)


if __name__ == "__main__":
    dayNumber = 6

    example = [
        "Time:      7  15   30",
        "Distance:  9  40  200",
    ]

    lines = get_input_lines(dayNumber)

    # Puzzle 1
    first_example = puzzle1(example)
    print("Example 1: " + str(first_example))

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    # Puzzle 2
    second_example = puzzle2(example)
    print("Example 2: " + str(second_example))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(puzzle2(lines)))
