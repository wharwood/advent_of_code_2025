from __future__ import annotations
from typing import Iterable, TypeVar, Optional, Generic

T = TypeVar("T", bound="grid_node")

class grid_node():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class grid(Generic[T]):
    def __init__(self, nodes: Optional[Iterable[T]] = None, limits: Optional[tuple[int, int, int, int]] = None) -> None:
        self.nodes: list[T] = list(nodes) if nodes is not None else []
        self.grid_bounds = None
        if limits is not None:
            self.grid_bounds = grid.bounds(limits[0], limits[1], limits[2], limits[3])
    
    class bounds:
        def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int) -> None:
            self.x_min = x_min
            self.x_max = x_max
            self.y_min = y_min
            self.y_max = y_max

        def __str__(self) -> str:
            return f"({self.x_min}, {self.x_max}, {self.y_min}, {self.y_max})"

    def get_len_x(self) -> int:
        return max([node.x for node in self.nodes]) - min([node.x for node in self.nodes]) + 1
    
    def get_len_y(self) -> int:
        return max([node.y for node in self.nodes]) - min([node.y for node in self.nodes]) + 1
    
    def get_max_x(self) -> int:
        return max([node.x for node in self.nodes if self.nodes is not None])
    
    def get_max_y(self) -> int:
        return max([node.y for node in self.nodes if self.nodes is not None])
    
    def get_min_x(self) -> int:
        return min([node.x for node in self.nodes if self.nodes is not None])
    
    def get_min_y(self) -> int:
        return min([node.y for node in self.nodes if self.nodes is not None])
    
    def is_in_grid(self, x: int, y: int) -> bool:
        return any(node.x == x and node.y == y for node in self.nodes)
    
    def get_node(self, x: int, y: int) -> Optional[T]:
        for node in self.nodes:
            if node.x == x and node.y == y:
                return node
        raise ValueError(f"No node at ({x},{y}).")

    def get_neighbors(self, node: T, diagonals: bool = False) -> list[T]:
        neighbors = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            x, y = node.x + dx, node.y + dy
            if self.is_in_grid(x, y):
                neighbors.append(self.get_node(x, y))
        if diagonals:
            diagonal_directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
            for dx, dy in diagonal_directions:
                x, y = node.x + dx, node.y + dy
                if self.is_in_grid(x, y):
                    neighbors.append(self.get_node(x, y))
        return neighbors

    def get_node_up(self, node: T) -> Optional[T] | None:
        neighbors = self.get_neighbors(node)
        for n in [n for n in neighbors if n is not None]:
            if n.x == node.x and n.y+1 == node.y:
                return n
        return None
    
    def get_node_down(self, node: T) -> Optional[T] | None:
        neighbors = self.get_neighbors(node)
        for n in [n for n in neighbors if n is not None]:
            if n.x == node.x and n.y-1 == node.y:
                return n
        return None
    
    def get_node_right(self, node: T) -> Optional[T] | None:
        neighbors = self.get_neighbors(node)
        for n in [n for n in neighbors if n is not None]:
            if n.x-1 == node.x and n.y == node.y:
                return n
        return None
    
    def get_node_left(self, node: T) -> Optional[T] | None:
        neighbors = self.get_neighbors(node)
        for n in [n for n in neighbors if n is not None]:
            if n.x+1 == node.x and n.y == node.y:
                return n
        return None