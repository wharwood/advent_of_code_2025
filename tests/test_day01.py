from pathlib import Path
from src.day01 import do_part_1, do_part_2
from src.helpers import helpers

def test_day01_part_1_example():
    file = Path("./tests/day01_example.txt")
    input = helpers.parse_input(file)
    assert do_part_1(input) == 3

def test_day01_part_2_example():
    file = Path("./tests/day01_example.txt")
    input = helpers.parse_input(file)
    assert do_part_2(input) == 6