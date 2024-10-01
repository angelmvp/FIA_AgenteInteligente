from src.environment.domain.environment import Environment
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map import Map


class EnvironmentService:
    """
    Provides services for the Environment class.
    
    Attributes:
        __terrain_repository (TerrainRepository): The terrain repository.
    """

    def __init__(self, terrain_repository: TerrainRepository):
        self.__terrain_repository = terrain_repository

    def create_environment_from_map(self, map: Map) -> Environment:
        """
        Creates an environment from a map.

        Args:
            map (Map): An instance of the Map class.

        Returns:
            Environment: An instance of the Environment class.
        """
        print(getattr(self, "__doc__", ""))
        return Environment(map)