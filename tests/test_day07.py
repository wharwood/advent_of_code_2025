from pathlib import Path
from src.day07 import do_part_1, do_part_2
from src.helpers import helpers

def test_day07_part_1_example():
    file = Path("./tests/day07_example.txt")
    input = helpers.parse_input(file)
    result = do_part_1(input)
    assert result == 21

def test_day07_part_2_example():
    file = Path("./tests/day07_example.txt")
    input = helpers.parse_input(file)
    result = do_part_2(input)
    assert result == 40