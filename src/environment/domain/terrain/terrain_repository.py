import json
from typing import Optional

from src.environment.domain.terrain.terrain import Terrain


class TerrainRepository:
    """Class that handles loading and accessing terrain data.

    Attributes:
        _terrain_dict (dict[int, Terrain]): A dictionary mapping terrain codes to Terrain objects.
    """

    def __init__(self):
        self._terrain_dict: dict[int, Terrain] = {}

    def load_from_file(self, file_path: str) -> None:
        """Loads terrain data from the JSON file at the given path and stores it in the terrain_dict attribute.

        Args:
            file_path (str): The path to the JSON file containing terrain data.

        Raises:
            FileNotFoundError: If the file at the given path does not exist.
        """
        with open(file_path, 'r') as file:
            terrain_data = json.load(file)

        for terrain_code, terrain_data in terrain_data.items():
            self._terrain_dict[int(terrain_code)] = Terrain(
                terrain_code,
                terrain_data['color'],
                terrain_data['display_name'],
                terrain_data['movement_costs'])

    def get_by_code(self, code: int) -> Optional[Terrain]:
        """Returns the Terrain object corresponding to the given code or None if the code is not found.

        Args:
            code (int): The code of the terrain to return.

        Returns:
            Terrain: The Terrain object corresponding to the given code or None if the code is not found.
        """
        return self._terrain_dict.get(code)

    def get_all(self) -> list[Terrain]:
        """Returns a list of all Terrain objects.

        Returns:
            list[Terrain]: A list of all Terrain objects.
        """
        return list(self._terrain_dict.values())
