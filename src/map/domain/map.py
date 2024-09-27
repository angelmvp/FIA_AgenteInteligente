from typing import List

from terrain import Terrain

class Cell:
    """Entidad que representa una celda en el mapa."""

    def __init__(self, x: int, y: int, terrain: Terrain):
        self.x = x
        self.y = y
        self.terrain = terrain
        self.flags = []

    def add_flag(self, flag: str) -> bool:
        if flag not in self.flags:
            self.flags.append(flag)
            return True
        return False

    def remove_flag(self, flag: str) -> bool:
        if flag in self.flags:
            self.flags.remove(flag)
            return True
        return False

    def has_flag(self, flag: str) -> bool:
        return flag in self.flags

    def __str__(self):
        return f"Cell(x={self.x}, y={self.y}, terrain={self.terrain})"

class Map:
    """Entidad que representa un mapa de terrenos."""

    def __init__(self, rows: int, columns: int, grid: List[List[Cell]]):
        self.grid = grid
        self.rows = rows
        self.columns = columns

    def get_cell(self, x: int, y: int) -> Cell:
        return self.grid[x][y]