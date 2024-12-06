# 2024 Advent of Code day 6

from pprint import pprint

from utils import get_input_lines


def move(i, j, map, direction):
    if direction == "^":
        if map[i - 1][j] == "#":
            return i, j, ">"
        else:
            return i - 1, j, direction
    elif direction == ">":
        if map[i][j + 1] == "#":
            return i, j, "v"
        else:
            return i, j + 1, direction
    elif direction == "v":
        if map[i + 1][j] == "#":
            return i, j, "<"
        else:
            return i + 1, j, direction
    elif direction == "<":
        if map[i][j - 1] == "#":
            return i, j, "^"
        else:
            return i, j - 1, direction


def guard_walk(map, max_iterations=10000):
    visited = set()
    iterations = 0
    updated_map = map.copy()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] in "^":
                x, y = i, j
                updated_map[x] = updated_map[x][:y] + "8" + updated_map[x][y + 1 :]
                visited.add((x, y))
                direction = map[i][j]
                while x > 0 and x < len(map) - 1 and y > 0 and y < len(map[0]) - 1:
                    x, y, direction = move(x, y, map, direction)
                    updated_map[x] = (
                        updated_map[x][:y] + direction + updated_map[x][y + 1 :]
                    )
                    # print_map(updated_map)
                    visited.add((x, y))
                    iterations += 1
                    if iterations >= max_iterations:
                        raise RuntimeError("Max iterations reached")

                break
    return visited


def puzzle1(lines):
    visited = guard_walk(lines)
    return len(visited)


def compute_block_coordinates(i, j, direction):
    if direction == "^":
        return i - 1, j
    elif direction == ">":
        return i, j + 1
    elif direction == "v":
        return i + 1, j
    elif direction == "<":
        return i, j - 1


def add_new_block(blocks):
    possible_coordinates = []
    for i in range(len(blocks) - 2):
        x, y = -1, -1
        first_block_direction = blocks[i][2]
        if first_block_direction == "^":
            x = blocks[i + 2][0] - 1
            y = blocks[i][1] - 1
        elif first_block_direction == ">":
            x = blocks[i][0] - 1
            y = blocks[i + 2][1] + 1
        elif first_block_direction == "v":
            x = blocks[i][0]
            y = blocks[i + 2][0] + 1

        if x > 0 and y > 0 and x < len(blocks) - 1 and y < len(blocks[0]) - 1:
            possible_coordinates.append((x, y))


def place_blocks(blocks):
    coordinates = []
    for i in range(len(blocks) - 2):
        x = blocks[i][0] + blocks[i + 2][0] - blocks[i + 1][0]
        y = blocks[i][1] + blocks[i + 2][1] - blocks[i + 1][1]
        coordinates.append((x, y))
    return coordinates


def get_blocks_coordinates(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] in "^":
                x, y = i, j
                direction = lines[i][j]
                directions = []
                while x > 0 and x < len(lines) - 1 and y > 0 and y < len(lines[0]) - 1:
                    new_x, new_y, new_direction = move(x, y, lines, direction)
                    if new_direction != direction:
                        block = compute_block_coordinates(x, y, direction)
                        directions.append(block)

                    x, y, direction = new_x, new_y, new_direction
                break
    return directions


def puzzle2(lines):
    blocks = get_blocks_coordinates(lines)
    print("Blocks coordinates")
    pprint(blocks)
    print()
    potential_blocks = place_blocks(blocks)
    print("Potential blocks")
    pprint(potential_blocks)

    counter = 0
    for pb in potential_blocks:
        i, j = pb
        map = lines.copy()
        map[i] = map[i][:j] + "#" + map[i][j + 1:]

        try:
            guard_walk(map, max_iterations=100000)
        except RuntimeError:
            print(i, j, "is a success, guard can't reach the exit.")
            counter += 1
            continue

    return counter


def print_map(map):
    for line in map:
        print("\t", line)


def test_new_block(lines, i, j):
    map = lines.copy()
    map[i] = map[i][:j] + "#" + map[i][j + 1:]

    try:
        guard_walk(map, max_iterations=100000)
    except RuntimeError:
        return True
    return False


def puzzle2_take2(lines):
    guard_x, guard_y = -1, -1
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] in "^":
                guard_x, guard_y = i, j
                break

    visited = guard_walk(lines, max_iterations=100000)
    visited -= {(guard_x, guard_y)}
    print("Guard visits ", len(visited), " coordinates")

    counter = 0
    for idx, coord in enumerate(visited):
        i, j = coord
        print("Testing ", idx, f"/{len(visited)}...", end="\r")
        if test_new_block(lines, i, j):
            counter += 1

    print()
    return counter


if __name__ == "__main__":
    dayNumber = 6

    example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    lines = get_input_lines(dayNumber)
    # lines = example.split("\n")

    # first_result = puzzle1(lines)
    # print("Puzzle 1: " + str(first_result))

    # second_result = puzzle2(lines)
    # print("Puzzle 2: " + str(second_result))

    print("------------")
    second_result = puzzle2_take2(lines)
    print("Puzzle 2: " + str(second_result))
