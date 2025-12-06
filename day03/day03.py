def do_part_1(input_lines):
    banks: list[BatteryBank] = []
    for line in input_lines:
        bank = BatteryBank()
        bank.parse_cell_str(line)
        banks.append(bank)
    result = 0
    for bank in banks:
        result += bank.get_max_joltage(2)
    print(f"Max joltage: {result}")

def do_part_2(input_lines):
    banks: list[BatteryBank] = []
    for line in input_lines:
        bank = BatteryBank()
        bank.parse_cell_str(line)
        banks.append(bank)
    result = 0
    for bank in banks:
        result += bank.get_max_joltage(12)
    print(f"Max joltage: {result}")

class BatteryBank:
    def __init__(self, cells: list[int] = []):
        self.cells = cells

    def parse_cell_str(self, cell_str: str):
        self.cells = [int(c) for c in cell_str]

    def get_max_joltage(self, cell_qty: int) -> int:
        stack = []
        drop = len(self.cells) - cell_qty
        for n in self.cells:
            while drop and stack and stack[-1] < n:
                stack.pop()
                drop -= 1
            stack.append(n)
        result = stack[:cell_qty]
        return int("".join(map(str, result)))
