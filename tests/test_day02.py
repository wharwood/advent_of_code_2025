from pathlib import Path
from src.day02 import do_part_1, do_part_2
from src.helpers import helpers

def test_day02_part_1_example():
    file = Path("./input/day02_example.txt")
    input = helpers.parse_input(file)
    assert do_part_1(input) == 1227775554

def test_day02_part_2_example():
    file = Path("./input/day02_example.txt")
    input = helpers.parse_input(file)
    assert do_part_2(input) == 4174379265