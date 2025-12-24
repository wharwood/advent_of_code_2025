from src import day01
from src import day02
from src import day03
from src import day04
from src import day05
from src import day06
from src import day07
from src.helpers import helpers

from pathlib import Path
import argparse
from types import ModuleType

def parse_args():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("-d", "--day", nargs="*", help="Day number to run. If not provided, runs all days.")
    parser.add_argument("-e", "--example", action="store_true", help="Use example input instead of actual input.")
    return parser.parse_args()

def main(selected_day=None, use_example=False):
    day_map: dict[str, ModuleType] = {
        "01": day01,
        "02": day02,
        "03": day03,
        "04": day04,
        "05": day05,
        "06": day06,
        "07": day07,
        }
    
    args = parse_args()
    if selected_day:
        days = [str(selected_day).zfill(2)]
    elif args.day:
        days = [str(d).zfill(2) for d in args.day]
    else:
        days = list(day_map.keys())

    for day_number in days:
        day_module = day_map.get(day_number)
        if day_module is None:
            raise ValueError(f"No module found for day {day_number}")
            continue
    
        if use_example or args.example:
            file_path = Path(f"./tests/day{day_number}_example.txt")
        else:
            file_path = Path(f"./input/day{day_number}_input.txt")

        input_lines = helpers.parse_input(file_path)

        part_1_result = day_module.do_part_1(input_lines)
        print(f"Day {day_number} - Part 1: {part_1_result}")

        part_2_result = day_module.do_part_2(input_lines)
        print(f"Day {day_number} - Part 2: {part_2_result}")

if __name__ == "__main__":
    main()