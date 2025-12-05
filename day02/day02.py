def do_part_1(input_lines):
    ranges = get_ranges(input_lines)
    sum = 0
    for r in ranges:
        for num in range(r[0], r[1] + 1):
            if is_two_repeated_digits(num):
                sum += num
    print(f"Sum of invalid inputs: {sum}")

def do_part_2(input_lines):
    ranges = get_ranges(input_lines)
    sum = 0
    for r in ranges:
        for num in range(r[0], r[1] + 1):
            if is_any_repeated_digits(num):
                sum += num
    print(f"Sum of invalid inputs: {sum}")

def get_ranges(input_lines) -> list[tuple[int, int]]:
    result = []
    for line in input_lines:
        ranges = line.split(",")
    for range in ranges:
        bounds = range.split("-")
        result.append((int(bounds[0]), int(bounds[1])))
    return result

def is_two_repeated_digits(num: int) -> bool:
    if len(str(num)) % 2 != 0:
        return False
    half = len(str(num)) // 2
    first_half = str(num)[:half]
    second_half = str(num)[half:]
    return first_half == second_half

def is_any_repeated_digits(num: int) -> bool:
    half = len(str(num)) // 2
    first_half = str(num)[:half]
    for i in range(len(first_half),0,-1):
        kernal = first_half[:i]
        if len(str(num)) % len(kernal) != 0:
            continue
        rest = str(num)[len(kernal):]
        if all(rest[j:j+len(kernal)] == kernal for j in range(0, len(rest), len(kernal))):
            return True
    return False