# Description Advent of Code day 5

from utils.utils import get_input_lines
from typing import List
import os


def parse_seeds(first_line):
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
    seeds = parse_seeds(lines[0])
    maps = parse_maps(lines[1:])
    return min(traverse_map(maps, seed) for seed in seeds)


# ------------------------------
# Puzzle 2
# ------------------------------

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end})"

def traverse_map_with_ranges(map, ranges:List[Range]):
    result = []
    for dest, src, size in map:
        src_end = src + size
        new_ranges = []
        while ranges:
            # [start                                 end)
            #           [src        src_end)
            # [ BEFORE ][ INSIDE           ][ AFTER ]
            start, end = ranges.pop()
            before = Range(start, min(end, src))
            inside = Range(max(start, src), min(end, src_end))
            after = Range(max(src_end, start), end)

            if before.start < before.end:
                new_ranges.append(before)
            if inside.start < inside.end:
                result.append(Range(inside.start - src + dest, inside.end - src + dest))
            if after.start < after.end:
                new_ranges.append(after)
        ranges = new_ranges
    return result + ranges


def traverse_maps_with_ranges(maps, ranges:List[Range]):
    final_ranges = []
    for map in maps:
        final_ranges.extend(traverse_map_with_ranges(map, ranges))
    print(final_ranges)
    return min(r.start for r in final_ranges)

        
        


def puzzle2(lines):
    seeds = parse_seeds(lines[0])
    ranges = [Range(start, start + size) for start, size in zip(seeds[::2], seeds[1::2])]
    maps = parse_maps(lines[1:])

    for r in ranges:
        traverse_maps_with_ranges(maps, [r])



    
    
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
    first_puzzle = puzzle1(lines)
    print("Puzzle 1: " + str(first_puzzle))
    print()

    # Puzzle 2
    second_example = puzzle2(example)
    print("Example 2: " + str(second_example))


