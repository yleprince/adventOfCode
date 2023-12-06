# Description Advent of Code day 5

from utils.utils import get_input_lines


def parse_seeds1(first_line):
    seeds_raw = first_line.split(": ")[1]
    return [int(x) for x in seeds_raw.split(" ")]


def line_contains_range(line):
    return line != "" and "map:" not in line


def parse_maps(lines):
    maps = []
    current_map = []
    for line in lines:
        if line_contains_range(line):
            dest, src, range_length = (int(el) for el in line.split(" "))
            current_map.append((dest, src, range_length))
        else:
            current_map = sorted(current_map, key=lambda x: x[1])
            maps.append(current_map)
            current_map = []
    maps.append(current_map)
    return [m for m in maps if m != []]


def traverse_map(maps, seed):
    for map in maps:
        for d, s, r in map:
            if s <= seed < s + r:
                seed += d - s
                break
    return seed


def puzzle1(lines):
    seeds = parse_seeds1(lines[0])
    maps = parse_maps(lines[1:])
    return min(traverse_map(maps, seed) for seed in seeds)


# ------------------------------
# Puzzle 2
# ------------------------------


def parse_seeds2(first_line):
    seeds_raw = first_line.split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds_raw]
    return {seeds[i]: seeds[i + 1] for i in range(0, len(seeds), 2)}


def convert_map_format(map):
    return [(s, s + r, d - s) for d, s, r in map]


def clean_map(map):
    return [(s, e, r) for s, e, r in map if s != e]


def merge_two_maps(first, second):
    merged = set()
    print("merged", merged)
    for s1, e1, r1 in first:
        print("\ts1, e1, r1", s1, e1, r1)
        for s2, e2, r2 in second:
            print("\t\ts2, e2, r2", s2, e2, r2)
            if e1 + r1 < s2 or s1 + r1 >= e2:  # A and E
                print("\t\tA or E")
                merged.add((s1, e1, r1))
                merged.add((s2, e2, r2))

            elif s1 + r1 >= s2 and e1 + r1 <= e2:  # F
                print("\t\tF")
                merged.add((s2, s1 + r1, r2))
                merged.add((e1 + r1, e2, r2))
                merged.add((s1, e1, r1 + r2))

            elif s1 + r1 < s2 and e1 + r1 >= e2:  # C
                print("\t\tC")
                merged.add((s2, e2, r2 + r1))
                merged.add((s1, s2 - r1, r1))
                merged.add((s2 - r1, e1, r1))

            elif s1 + r1 < s2 and s2 <= e1 + r1 <= e2:  # B
                print("\t\tB")
                merged.add((s1, s2 - r1, r1))
                merged.add((s2 - r1, e1, r1 + r2))
                merged.add((s2, e2, r2))

            elif s2 <= s1 + r1 < e2 and e1 + r1 >= e2:  # D
                print("\t\tD")
                merged.add((s2, s1 + r1, r2))
                merged.add((e2, e1 + r1, r1))
                merged.add((s1 + r1, e2, r1 + r2))
            display = sorted(clean_map(list(merged)))
            print("merged", display)
            print()
    return merged


# def merge_two_maps2(first, second):
#    merged = list()
#    for s1, e1, r1 in first:
#        S1, E1 = s1 + r1, e1 + r1
#        for s2, e2, r2 in second:

#            elif s1 + r1 < s2 and s2 <= e1 + r1 < e2:
#                bound = e1 + r1 - s2
#                merged.add((s1, bound, r1))
#                merged.add((bound, e1, r1 + r2))
#                merged.add((e1, e2, r2))
#            elif s1 + r1 >= s2 and e1 + r1 >= e2:
#                merged.add((s1, e1 + r1 - e2, r1 + r2))
#                merged.add((e1 + r1 - e2, e1, r1))
#                merged.add((s2, e1 + r1 - e2, r2))


def merge_maps(maps):
    while len(maps) > 1:
        first = maps.pop(0)
        second = maps.pop(0)
        merged = merge_two_maps(first, second)
        maps = [merged] + maps
    return maps


def puzzle2(lines):
    seeds = parse_seeds2(lines[0])
    maps = parse_maps(lines[1:])
    converted_maps = [convert_map_format(m) for m in maps]
    print()
    print(converted_maps)
    print()
    first, second = converted_maps[0], converted_maps[1]
    print("first", first)
    print("second", second)
    print()
    result = merge_two_maps(first, second)
    result = sorted(list(result))
    print(result)
    print()

    #    merged_maps = merge_maps(converted_maps)

    return 0


if __name__ == "__main__":
    dayNumber = 5

    example = [
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    ]

    lines = get_input_lines(dayNumber)

    # Puzzle 1
    first_example = puzzle1(example)
    print("Example 1: " + str(first_example))

    #    first_result = puzzle1(lines)
    #    print("Puzzle 1: " + str(first_result))
    #    print()

    # Puzzle 2
    second_example = puzzle2(example)
    print("Example 2: " + str(second_example))
#
#    second_result = puzzle2(lines)
#    print("Puzzle 2: " + str(second_result))
