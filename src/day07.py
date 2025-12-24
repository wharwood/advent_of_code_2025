from __future__ import annotations
from collections import deque
from .grid import grid, grid_node

def do_part_1(lines: list[str]) -> int:
    grid = make_tachyon_grid(lines)
    splits = grid.get_splits()
    return splits

def do_part_2(lines: list[str]) -> int:
    pass

def make_tachyon_grid(input_lines) -> tachyon_grid:
    nodes: list[tachyon_node] = []
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line.rstrip()):
            nodes.append(tachyon_node(x, y, char))
    return tachyon_grid(nodes)

class tachyon_node(grid_node):
    def __init__(self, x: int, y: int, contents: str) -> None:
        super().__init__(x, y)
        if contents not in ['.', 'S', '^']:
            raise ValueError(f"Invalid contents for tachyon node: {contents}")
        self.contents = contents

    def __repr__(self) -> str:
        return super().__repr__() + f" {self.contents}"

class tachyon_grid(grid):
    def __init__(self, nodes: list[tachyon_node]) -> None:
        super().__init__(nodes)

    def get_splits(self) -> int:
        start_nodes: deque[tachyon_node] = deque([n for n in self.nodes if n.contents == 'S'])
        splits = 0
        while start_nodes:
            current_node = start_nodes.popleft()
            while current_node:
                if current_node.contents == '^':
                    splits += 1
                    right_node = self.get_node_right(current_node)
                    if right_node and right_node.contents == '.':
                        start_nodes.append(right_node)
                    left_node = self.get_node_left(current_node)
                    if left_node and left_node.contents == '.':
                        start_nodes.append(left_node)
                    break
                elif current_node.contents == '|':
                    break
                elif current_node.contents == 'S':
                    current_node = self.get_node_down(current_node)
                else:
                    current_node.contents = '|'
                    current_node = self.get_node_down(current_node)
        return splits
