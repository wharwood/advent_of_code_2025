from pathlib import Path
from src.day04 import do_part_1, do_part_2
from src.helpers import helpers

def test_day04_part_1_example():
    file = Path("./input/day04_example.txt")
    input = helpers.parse_input(file)
    assert do_part_1(input) == 13

def test_day04_part_2_example():
    file = Path("./input/day04_example.txt")
    input = helpers.parse_input(file)
    assert do_part_2(input) == 43