import os
from src.map.domain.map import Map



class MapRepository:
    """
    Class that handles the loading and access to map data.

    Attributes:
        __directory_path (str): The directory path where map files are stored.
    """

    def __init__(self, directory_path: str):
        """
        Initializes a MapRepository instance.

        Args:
            directory_path (str): The directory path where map files are stored.
        """
        self.__directory_path: str = directory_path

    @staticmethod
    def load_from_txt(file_path: str) -> Map:
        """
        Loads a map from a text file.

        Args:
            file_path (str): The path to the text file.

        Returns:
            Map: An instance of the Map class with the loaded data.
        """
        with open(file_path) as file:
            grid: list[list[int]] = [[int(cell) for cell in row.split()] for row in file]
            rows: int = len(grid)
            columns: int = len(grid[0]) if rows > 0 else 0
            return Map(grid, rows, columns)

    @staticmethod
    def load_from_csv(file_path: str) -> Map:
        """
        Loads a map from a CSV file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            Map: An instance of the Map class with the loaded data.
        """
        with open(file_path) as file:
            grid: list[list[int]] = [[int(cell) for cell in row.split(',')] for row in file]
            rows: int = len(grid)
            columns: int = len(grid[0]) if rows > 0 else 0
            return Map(grid, rows, columns)

    def load(self, name: str) -> Map:
        """
        Loads a map by its name.

        Args:
            name (str): The name of the map file.

        Returns:
            Map: An instance of the Map class with the loaded data.

        Raises:
            ValueError: If the file format is unsupported.
        """
        file_path: str = f"{self.__directory_path}/{name}"
        file_extension: str = os.path.splitext(file_path)[1]

        if file_extension == '.txt':
            return MapRepository.load_from_txt(file_path)
        elif file_extension == '.csv':
            return MapRepository.load_from_csv(file_path)
        else:
            raise ValueError("Unsupported file format")