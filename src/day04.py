from __future__ import annotations
from .grid import grid, grid_node

def do_part_1(input_lines: list[str]) -> int:
    grid = make_factory(input_lines)
    accessible_count = 0
    for node in grid.nodes:
        if not node.is_paper():
            continue
        if grid.is_accessible(node):
            accessible_count += 1
    return accessible_count

def do_part_2(input_lines: list[str]) -> int:
    grid = make_factory(input_lines)
    accessible_count = 0
    iteration = 0
    while True:
        iteration += 1
        accessible_nodes = []
        for node in grid.nodes:
            if not node.is_paper():
                continue
            if grid.is_accessible(node):
                accessible_nodes.append(node)
        if not accessible_nodes:
            break
        accessible_count += len(accessible_nodes)
        grid.remove_paper(accessible_nodes)
    return accessible_count

def make_factory(input_lines) -> paper_factory_grid:
    nodes: list[paper_factory_node] = []
    for y, line in enumerate(input_lines):
        for x, char in enumerate(line.rstrip()):
            nodes.append(paper_factory_node(x, y, char))
    return paper_factory_grid(nodes)

class paper_factory_node(grid_node):
    def __init__(self, x: int, y: int, contents: str) -> None:
        super().__init__(x, y)
        if contents not in ['.', '@']:
            raise ValueError(f"Invalid contents for paper factory node: {contents}")
        self.contents = contents

    def is_paper(self) -> bool:
        return self.contents == '@'
    
class paper_factory_grid(grid[paper_factory_node]):
    def __init__(self, nodes: list[paper_factory_node]) -> None:
        super().__init__(nodes)

    def is_accessible(self, node: paper_factory_node, surround_qty_limit: int = 4) -> bool:
        if not node.is_paper():
            raise ValueError("Node is not paper.")
        neighbors = self.get_neighbors(node, diagonals=True)
        if len([n for n in neighbors if n.is_paper()]) < surround_qty_limit:
            return True
        return False
    
    def remove_paper(self, nodes: list[paper_factory_node]) -> None:
        for node in nodes:
            if not node.is_paper():
                raise ValueError("Node is not paper.")
            node.contents = '.'