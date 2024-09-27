import json
from typing import Dict


class Terrain:
    """Entidad que representa un tipo de terreno en el mapa."""

    def __init__(self, display_name: str, color: str, movement_costs: Dict[str, int]):
        self.display_name = display_name
        self.color = color
        self.movement_costs = movement_costs

    def get_movement_cost(self, movement_type: str) -> int or None:
        """
        Retorna el costo de movimiento para un tipo de movimiento.

        Args:
            movement_type (str): Tipo de movimiento.

        Returns:
            int or None: Costo de movimiento.
        """
        return self.movement_costs.get(movement_type)

    def __str__(self):
        return f"Terrain(display_name={self.display_name}, color={self.color}, movement_costs={self.movement_costs})"


class TerrainRepository:
    """Clase que maneja la carga y acceso a los datos de los terrenos."""

    def __init__(self, file_path: str):
        self.file_path = file_path
        self.terrain_dict = self.__load_terrain_data()

    def __load_terrain_data(self) -> Dict[int, Terrain]:
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            return {int(key): Terrain(value['display_name'], value['color'], value['movement_costs']) for key, value in
                    data.items()}

    def get(self, code: int) -> Terrain:
        """Retorna un terreno según su código."""
        return self.terrain_dict.get(code)
