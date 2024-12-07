# 2024 Advent of Code day 7

from utils import get_input_lines


def process_input(lines):
    output = []
    for line in lines:
        result, equation = line.split(": ")
        equation = [int(v) for v in equation.split(" ")]
        output.append((int(result), equation))
    return output


def equation_is_valid(result, equation) -> bool:
    buffer = [equation.pop(0)]
    while equation:
        current = equation.pop(0)
        new_buffer = []
        for intermediate_result in buffer:
            new_buffer.append(current + intermediate_result)
            new_buffer.append(current * intermediate_result)
        buffer = new_buffer
    return result in buffer


def equation2_is_valid(result, equation) -> bool:
    buffer = [equation.pop(0)]
    while equation:
        current = equation.pop(0)
        new_buffer = []
        for intermediate_result in buffer:
            new_buffer.append(current + intermediate_result)
            new_buffer.append(current * intermediate_result)
            new_buffer.append(int(str(intermediate_result) + str(current)))
        buffer = new_buffer
    return result in buffer


def puzzle1(lines):
    processed = process_input(lines)
    counter = 0
    for line in processed:
        if equation_is_valid(line[0], line[1]):
            counter += line[0]
    return counter


def puzzle2(lines):
    processed = process_input(lines)
    counter = 0
    for line in processed:
        if equation2_is_valid(line[0], line[1]):
            counter += line[0]
    return counter


if __name__ == "__main__":
    dayNumber = 7

    example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

    lines = get_input_lines(dayNumber)
    # lines = example.split("\n")

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
