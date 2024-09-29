class Map:
    """Entidad que representa un mapa de terrenos."""

    def __init__(self, rows: int, columns: int, grid: list[list[int]]):
        self.grid = grid
        self.rows = rows
        self.columns = columns

    def get_cell(self, x: int, y: int) -> int:
        return self.grid[x][y]

    def print(self):
        for row in self.grid:
            print(row)
