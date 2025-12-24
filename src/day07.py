from __future__ import annotations
from collections import deque
from functools import lru_cache
from .grid import grid, grid_node

def do_part_1(lines: list[str]) -> int:
    grid = make_tachyon_grid(lines)
    splits = grid.get_splits()
    return splits

def do_part_2(lines: list[str]) -> int:
    grid = make_tachyon_grid(lines)
    unique_paths = grid.get_unique_path_count()
    return unique_paths

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

    def get_start_node(self) -> tachyon_node:
        for node in self.nodes:
            if node.contents == 'S':
                return node
        raise ValueError("No start node found.")

    def get_splits(self) -> int:
        start_nodes = deque([self.get_start_node()])
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
    
    def get_unique_path_count(self) -> int:
        start = self.get_start_node()

        @lru_cache(maxsize=None)
        def count_from(coord: tuple[int, int]) -> int:
            current_node = self.get_node(*coord)
            if current_node is None:
                return 0
            if current_node.contents not in ('.', 'S', '^'):
                return 0

            below = self.get_node_down(current_node)
            if below is None:
                return 1

            if current_node.contents == '^':
                total = 0
                left = self.get_node_left(current_node)
                if left and left.contents == '.':
                    total += count_from((left.x, left.y))
                right = self.get_node_right(current_node)
                if right and right.contents == '.':
                    total += count_from((right.x, right.y))
                return total

            # normal beam: continue down
            return count_from((below.x, below.y))

        return count_from((start.x, start.y))