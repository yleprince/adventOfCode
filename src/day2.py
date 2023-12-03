# Description Advent of Code day 2

from utils.utils import get_input_lines


def parse_line(line):
    parsed_line = dict()

    game, draws = line.split(": ")
    draws = draws.replace(";", ",").split(", ")
    game_id = int(game.split(" ")[1])
    for draw in draws:
        number, color = draw.split(" ")
        parsed_line[color] = max(parsed_line.get(color, 0), int(number))
    return (game_id, parsed_line)


def puzzle1(lines, constraint):
    counter = 0
    for line in lines:
        game, parsed_line = parse_line(line)
        checks = [nu <= constraint[color] for color, nu in parsed_line.items()]
        counter += game if all(checks) else 0
    return counter


def puzzle2(lines):
    counter = 0
    for line in lines:
        game, parsed_line = parse_line(line)
        powerCubes = (
            parsed_line.get("red", 0)
            * parsed_line.get("green", 0)
            * parsed_line.get("blue", 0)
        )
        counter += powerCubes
    return counter


if __name__ == "__main__":
    dayNumber = 2
    lines = get_input_lines(dayNumber)

    # Puzzle 1
    constraint = {"red": 12, "green": 13, "blue": 14}

    first_result = puzzle1(lines, constraint)
    print("Puzzle 1: " + str(first_result))

    # Puzzle 2
    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
