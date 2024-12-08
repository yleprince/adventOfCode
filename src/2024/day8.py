# 2024 Advent of Code day 8

from utils import get_input_lines


def puzzle1(lines):
    array = "".join(lines)
    coords = set()
    l, L = len(lines[0]), len(lines)

    for i in range(len(array) - 1):
        if array[i] not in ".#":
            i_x = i % l
            i_y = i // l
            for j in range(i + 1, len(array)):
                if array[j] == array[i]:
                    j_x = j % l
                    j_y = j // l
                    c0 = (i_x - (j_x - i_x), i_y - (j_y - i_y))
                    c1 = (j_x + (j_x - i_x), j_y + (j_y - i_y))
                    if c0[0] >= 0 and c0[1] >= 0 and c0[0] < l and c0[1] < L:
                        coords.add(c0)
                    if c1[0] >= 0 and c1[1] >= 0 and c1[0] < l and c1[1] < L:
                        coords.add(c1)
    return len(coords)


def point_is_within_boundaries(pt, l, L):
    x, y = pt
    return x >= 0 and y >= 0 and x < l and y < L


def compute_coords(pt0, pt1, l, L):
    coords = set()
    x0, y0 = pt0
    x1, y1 = pt1
    dx = x1 - x0
    dy = y1 - y0
    c0 = (x0 - dx, y0 - dy)
    while point_is_within_boundaries(c0, l, L):
        coords.add(c0)
        c0 = (c0[0] - dx, c0[1] - dy)
    c1 = (x1 + dx, y1 + dy)
    while point_is_within_boundaries(c1, l, L):
        coords.add(c1)
        c1 = (c1[0] + dx, c1[1] + dy)
    return coords


def puzzle2(lines):
    array = "".join(lines)
    coords = set()
    l, L = len(lines[0]), len(lines)

    for i in range(len(array) - 1):
        if array[i] not in ".#":
            i_x = i % l
            i_y = i // l
            for j in range(i + 1, len(array)):
                if array[j] == array[i]:
                    coords.add((i_x, i_y))
                    j_x = j % l
                    j_y = j // l
                    coords.add((j_x, j_y))
                    coords = coords.union(compute_coords((i_x, i_y), (j_x, j_y), l, L))

    return len(coords)


if __name__ == "__main__":
    dayNumber = 8

    example = """......#....#
...#....0...
....#0....#.
..#....0....
....0....#..
.#....A.....
...#........
#......#....
........A...
.........A..
..........#.
..........#."""

    example0 = """..........
...#......
..........
....a.....
..........
.....a....
..........
......#...
..........
.........."""

    example1 = """T....#....
...T......
.T....#...
.........#
..#.......
..........
...#......
..........
....#.....
.........."""

    lines = get_input_lines(dayNumber)
    # lines = example.split("\n")

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
