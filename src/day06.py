def do_part_1(input_lines):
    cols, operations = parse_input_part_1(input_lines)
    results = []
    for i, col in enumerate(cols):
        if operations[i] == "+":
            result = add_list(col)
        elif operations[i] == "*":
            result = multiply_list(col)
        else:
            raise ValueError(f"Unknown operation: {operations[i]}")
        results.append(result)
    return sum(results)

def do_part_2(input_lines):
    cols, operations = parse_input_part_2(input_lines)
    results = []
    for i, col in enumerate(cols):
        if operations[i] == "+":
            result = add_list(col)
        elif operations[i] == "*":
            result = multiply_list(col)
        else:
            raise ValueError(f"Unknown operation: {operations[i]}")
        results.append(result)
    return sum(results)

def parse_input_part_1(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    cols = [[int(x) for x in col] for col in zip(*(row.split() for row in lines[:-1]))]
    operations = [line for line in lines[-1].split()]
    return cols, operations

def parse_input_part_2(lines: list[str]) -> tuple[list[list[int]], list[str]]:
    cols: list[str] = []
    operations: list[str] = []
    for row_idx, row in enumerate(lines):
        for col_idx, char in enumerate(row):
            if row_idx == 0:
                cols.append(char)
            elif row_idx == len(lines) - 1:
                if char != " ":
                    operations.append(char)
            else:
                cols[col_idx] += char
    next_group = []
    separated_cols: list[list[int]] = []
    for col in cols:
        if col.strip() == "":
            if next_group:
                separated_cols.append(next_group)
                next_group = []
        else:
            next_group.append(int(col.strip()))
    return separated_cols, operations

def add_list(lst: list[int]) -> int:
    return sum(lst)

def multiply_list(lst: list[int]) -> int:
    result = 1
    for num in lst:
        result *= num
    return result