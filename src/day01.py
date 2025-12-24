def do_part_1(input_lines: list[str]) -> int:
    start = 50
    zeros = 0
    while True:
        for line in input_lines:
            direction = line[0]
            count = int(line[1:])
            end = do_rotation(start, direction, count)
            if end == 0:
                zeros += 1
            start = end
        break
    return zeros

def do_part_2(input_lines: list[str]) -> int:
    start = 50
    zeros = 0
    moves = get_moves(input_lines)
    for move in moves:
        if move == "R":
            start += 1
        else:
            start -= 1
        if start < 0:
            start = 100 + start
        start = start % 100
        if start == 0:
            zeros += 1
    return zeros

def do_rotation(start: int, direction: str, count: int) -> int:
    if direction == "R":
        start += count
    else:
        start -= count
    if start < 0:
        start = 100 + start
    start = start % 100
    return start

def get_moves(input_lines) -> list[str]:
    moves = []
    for line in input_lines:
        direction = line[0]
        count = int(line[1:])
        for _ in range(count):
            moves.append(direction)
    return moves