from __future__ import annotations
from typing import Iterable, TypeVar, Optional, Generic

T = TypeVar("T", bound="grid_node_3d")

class grid_node_3d():
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
class grid_3d(Generic[T]):
    def __init__(
        self, 
        nodes: Optional[Iterable[T]] = None, 
        limits: Optional[tuple[int,int,int,int,int,int]] = None
    ) -> None:
        self.nodes: list[T] = list(nodes) if nodes is not None else []
        self.bounds = None
        if limits is not None:
            self.bounds = grid_3d.bounds_3d(limits[0], limits[1], limits[2], limits[3], limits[4], limits[5])

    class bounds_3d:
        def __init__(self, x_min: int, x_max: int, y_min: int, y_max: int, z_min: int, z_max: int) -> None:
            self.x_min = x_min
            self.x_max = x_max
            self.y_min = y_min
            self.y_max = y_max
            self.z_min = z_min
            self.z_max = z_max

        def __str__(self) -> str:
            return f"({self.x_min}, {self.x_max}, {self.y_min}, {self.y_max}, {self.z_min}, {self.z_max})"
        
    def get_distance(self, node_a: T, node_b: T) -> float:
        return ((node_a.x - node_b.x) ** 2 + (node_a.y - node_b.y) ** 2 + (node_a.z - node_b.z) ** 2) ** 0.5
        
    def get_closest_neighbors(self, node: T) -> list[T]:
        closest_neighbors: dict[T, float] = {}
        for node in self.nodes:
            if closest_neighbors is {}:
                closest_neighbors[node] = self.get_distance(node, node)