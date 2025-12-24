from pathlib import Path
from src.day03 import do_part_1, do_part_2
from src.helpers import helpers

def test_day03_part_1_example():
    file = Path("./tests/day03_example.txt")
    input = helpers.parse_input(file)
    assert do_part_1(input) == 357

def test_day03_part_2_example():
    file = Path("./tests/day03_example.txt")
    input = helpers.parse_input(file)
    assert do_part_2(input) == 3121910778619