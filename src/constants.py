import os

DIGITS_STR = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

COOKIES = {
    "session": os.environ.get("AOC_SESSION"),
    "_ga_MHSNPJKWC7": os.environ.get("AOC__GA__"),
    "_gid": os.environ.get("AOC__GID"),
    "_ga": os.environ.get("AOC__GA"),
}
