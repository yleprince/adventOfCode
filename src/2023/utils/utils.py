import requests

from .constants import COOKIES


def get_input_lines(dayNumber):
    url = "https://adventofcode.com/2023/day/" + str(dayNumber) + "/input"
    r = requests.get(url, cookies=COOKIES)
    return r.text.splitlines()
