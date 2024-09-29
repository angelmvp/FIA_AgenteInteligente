import json

from src.environment.domain.terrain.terrain import Terrain


class TerrainRepository:
    """Clase que maneja la carga y acceso a los datos de los terrenos."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.terrain_dict = self.__load_terrain_data()

    def __load_terrain_data(self) -> dict[int, Terrain]:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return {int(key): Terrain(value['display_name'], value['color'], value['movement_costs']) for key, value in
                    data.items()}

    def get(self, code: int) -> Terrain:
        """Retorna un terreno según su código."""
        return self.terrain_dict.get(code)
