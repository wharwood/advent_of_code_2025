from __future__ import annotations

def do_part_1(input_lines):
    fresh_count = 0
    fresh_ingredients, ingredients = parse_input(input_lines)
    fresh_ranges = [IntegerRange(start, end) for start, end in fresh_ingredients]
    fresh_ranges.sort(key=lambda r: r.start)
    merged_fresh_ranges = merge_ranges(fresh_ranges)
    for ingredient in ingredients:
        is_fresh = False
        for fresh_range in merged_fresh_ranges:
            if fresh_range.start <= ingredient <= fresh_range.end:
                is_fresh = True
                break
        if is_fresh:
            fresh_count += 1
    print(f"Fresh ingredients: {fresh_count}")

def do_part_2(input_lines):
    fresh_ingredients, _ = parse_input(input_lines)
    fresh_ranges = [IntegerRange(start, end) for start, end in fresh_ingredients]
    fresh_ranges = merge_ranges(fresh_ranges)
    print(f"Fresh ids: {sum(r.len() for r in fresh_ranges)}")

def parse_input(lines: list[str]) -> tuple[list[tuple[int,int]], list[int]]:
    start = True
    fresh_ingredients: list[tuple[int,int]] = []
    ingredient_ids: list[int] = []
    for line in lines:
        if line == "":
            start = False
            continue
        if start:
            parts = line.split("-")
            start = int(parts[0])
            end = int(parts[1])
            fresh_ingredients.append((start, end))
        else:
            ingredient_ids.append(int(line))
    return fresh_ingredients, ingredient_ids

class IntegerRange:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def has_overlap(self, other: IntegerRange) -> bool:
        return not (self.end < other.start or self.start > other.end)
    
    def merge(self, other: IntegerRange) -> IntegerRange:
        if not self.has_overlap(other):
            raise ValueError("Ranges do not overlap.")
        return IntegerRange(min(self.start, other.start), max(self.end, other.end))
    
    def len(self) -> int:
        return self.end - self.start + 1
    
def merge_ranges(ranges: list[IntegerRange]) -> list[IntegerRange]:
    if not ranges:
        return []
    ranges.sort(key=lambda r: r.start)
    merged_ranges: list[IntegerRange] = []
    current_range = ranges[0]
    for next_range in ranges[1:]:
        if current_range.has_overlap(next_range):
            current_range = current_range.merge(next_range)
        else:
            merged_ranges.append(current_range)
            current_range = next_range
    merged_ranges.append(current_range)
    return merged_ranges