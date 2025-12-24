from src import day01
from src import day02
from src import day03
from src import day04
from src import day05
from src import day06
from src.helpers import helpers

from pathlib import Path

def main():
    for day_module, day_number in [
        (day01, "01"),
        (day02, "02"),
        (day03, "03"),
        (day04, "04"),
        (day05, "05"),
        (day06, "06"),
    ]:
        file_path = Path(f"./input/day{day_number}_input.txt")
        input_lines = helpers.parse_input(file_path)

        part_1_result = day_module.do_part_1(input_lines)
        print(f"Day {day_number} - Part 1: {part_1_result}")

        part_2_result = day_module.do_part_2(input_lines)
        print(f"Day {day_number} - Part 2: {part_2_result}")

if __name__ == "__main__":
    main()