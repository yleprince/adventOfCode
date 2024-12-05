# 2024 Advent of Code day 5

from utils import get_input_lines


def parse_input(lines):
    rules = {}
    updates = []
    for line in lines:
        if "|" in line:
            left, right = line.split("|")
            left = int(left)
            right = int(right)
            rules.update({left: rules.get(left, []) + [right]})
        elif "," in line:
            updates.append([int(el) for el in line.split(",")])
    return rules, updates


def puzzle1(lines):
    rules, updates = parse_input(lines)
    counter = 0
    for update in updates:
        middle = update[len(update) // 2]
        start = update.pop(0)
        is_valid = True
        while update:
            next = update.pop(0)
            if start not in rules.keys() or next not in rules[start]:
                is_valid = False
                break
            start = next

        if is_valid:
            counter += middle
    return counter


def is_pair_valid(rules, update, i, j):
    return not (update[i] not in rules.keys() or update[j] not in rules[update[i]])


def fix_pair(update, i, j):
    update_ = update.copy()
    update_.insert(i, update_.pop(j))
    return update_


def puzzle2(lines):
    rules, updates = parse_input(lines)

    counter = 0
    for update in updates:
        idx = 0
        fixed = False
        while idx < len(update) - 1:
            if not is_pair_valid(rules, update, idx, idx + 1):
                update = fix_pair(update, idx, idx + 1)
                idx = 0
                fixed = True
            else:
                idx += 1
        if fixed:
            counter += update[len(update) // 2]

    return counter


if __name__ == "__main__":
    dayNumber = 5

    example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    lines = get_input_lines(dayNumber)
    # lines = example.split("\n")

    first_result = puzzle1(lines)
    print("Puzzle 1: " + str(first_result))

    second_result = puzzle2(lines)
    print("Puzzle 2: " + str(second_result))
