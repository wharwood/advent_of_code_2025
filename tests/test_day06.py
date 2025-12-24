from pathlib import Path
from src.day06 import do_part_1, do_part_2
from src.helpers import helpers

def test_day06_part_1_example():
    file = Path("./tests/day06_example.txt")
    input = helpers.parse_input(file)
    result = do_part_1(input)
    assert result == 4277556

def test_day06_part_2_example():
    file = Path("./tests/day06_example.txt")
    input = helpers.parse_input(file)
    result = do_part_2(input)
    assert result == 3263827