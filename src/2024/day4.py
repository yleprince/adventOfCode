# 2024 Advent of Code day 4
from utils import get_input_lines


def check_xmas(lines, i, j):
    count = 0

    # line left
    if j >= 3 and lines[i][j - 3:j] == "SAM":
        count += 1

    # diagonal up left
    if (
        j >= 3
        and i >= 3
        and lines[i - 1][j - 1] == "M"
        and lines[i - 2][j - 2] == "A"
        and lines[i - 3][j - 3] == "S"
    ):
        count += 1

    # line up
    if (
        i >= 3
        and lines[i - 1][j] == "M"
        and lines[i - 2][j] == "A"
        and lines[i - 3][j] == "S"
    ):
        count += 1

    # line right
    if j <= len(lines[0]) - 3 and lines[i][1 + j:j + 4] == "MAS":
        count += 1

    # diagonal up right
    if (
        j <= len(lines[0]) - 3
        and i >= 3
        and lines[i - 1][j + 1] == "M"
        and lines[i - 2][j + 2] == "A"
        and lines[i - 3][j + 3] == "S"
    ):
        count += 1

    # line down
    if (
        i <= len(lines) - 4
        and lines[i + 1][j] == "M"
        and lines[i + 2][j] == "A"
        and lines[i + 3][j] == "S"
    ):
        count += 1

    # diagonal down left
    if (
        j >= 3
        and i <= len(lines) - 3
        and lines[i + 1][j - 1] == "M"
        and lines[i + 2][j - 2] == "A"
        and lines[i + 3][j - 3] == "S"
    ):
        count += 1

    # diagonal down right
    if (
        j <= len(lines[0]) - 4
        and i <= len(lines) - 4
        and lines[i + 1][j + 1] == "M"
        and lines[i + 2][j + 2] == "A"
        and lines[i + 3][j + 3] == "S"
    ):
        count += 1
    return count


def check_x_mas(lines, i, j):
    # diag \
    if (
        lines[i - 1][j - 1] == "M"
        and lines[i + 1][j + 1] == "S"
        or lines[i - 1][j - 1] == "S"
        and lines[i + 1][j + 1] == "M"
    ):
        # diag /
        if (
            lines[i - 1][j + 1] == "M"
            and lines[i + 1][j - 1] == "S"
            or lines[i - 1][j + 1] == "S"
            and lines[i + 1][j - 1] == "M"
        ):
            return 1
    return 0


def puzzle1(lines):
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == "X":
                count += check_xmas(lines, i, j)
    return count


def puzzle2(lines):
    count = 0
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            if lines[i][j] == "A":
                count += check_x_mas(lines, i, j)
    return count


if __name__ == "__main__":
    dayNumber = 4

    example0 = """..X...
        .SAMX.
        .A..A.
        XMAS.S
        .X...."""

    example1 = """XMASAMX
        MM...MM
        A.A.A.A
        S..S..S
        A.A.A.A
        MM...MM
        XMASAMX"""

    example = """....XXMAS.
        .SAMXMS...
        ...S..A...
        ..A.A.MS.X
        XMASAMX.MM
        X.....XA.A
        S.S.S.S.SS
        .A.A.A.A.A
        ..M.M.M.MM
        .X.X.XMASX"""
    example = [e.strip() for e in example.split("\n")]

    lines = get_input_lines(dayNumber)
    # lines = example

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    example = """.M.S......
        ..A..MSMS.
        .M.S.MAA..
        ..A.ASMSM.
        .M.S.M....
        ..........
        S.S.S.S.S.
        .A.A.A.A..
        M.M.M.M.M.
        .........."""
    example = [e.strip() for e in example.split("\n")]
    # lines = example

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
