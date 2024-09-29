import os
from src.map.domain.map import Map

class MapRepository:
    """Clase que maneja la carga y acceso a los datos de los mapas."""

    def __init__(self, directory_path: str):
        self.directory_path = directory_path

    def load(self, name: str) -> Map:
        file_path = f"{self.directory_path}/{name}"
        file_extension = os.path.splitext(file_path)[1]

        if file_extension == '.txt':
            return self.__load_from_txt(file_path)
        elif file_extension == '.csv':
            return self.__load_from_csv(file_path)
        else:
            raise ValueError("Unsupported file format")

    def __load_from_txt(self, file_path: str) -> Map:
        with open(file_path) as file:
            rows, columns = map(int, file.readline().split())
            grid = [[int(cell) for cell in row.split()] for row in file]
            return Map(rows, columns, grid)

    def __load_from_csv(self, file_path: str) -> Map:
        with open(file_path) as file:
            grid = [[int(cell) for cell in row.split(',')] for row in file]
            rows = len(grid)
            columns = len(grid[0]) if rows > 0 else 0
            return Map(rows, columns, grid)