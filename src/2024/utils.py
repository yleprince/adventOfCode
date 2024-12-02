import os

import requests
from dotenv import load_dotenv

load_dotenv()

COOKIES = {
    "session": os.environ.get("session"),
    "_ga_MHSNPJKWC7": os.environ.get("_ga_MHSNPJKWC7"),
    "_gid": os.environ.get("_gid"),
    "_ga": os.environ.get("_ga"),
}


def get_input_lines(dayNumber):
    url = "https://adventofcode.com/2024/day/" + str(dayNumber) + "/input"
    r = requests.get(url, cookies=COOKIES)
    return r.text.splitlines()
