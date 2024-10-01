from typing import Optional

from src.environment.domain.cell.cell import Cell
from src.environment.domain.environment import Environment
from src.environment.domain.terrain.terrain import Terrain
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

  def print_discovered_map(self, environment: Environment):
    """
    Prints the environment.

    Args:
        environment (Environment): An instance of the Environment class.
    """
    for column in range(environment.get_columns()):
      for row in range(environment.get_rows()):
        if environment.is_discovered(row, column):
          print('D', end=' ')
        else:
          print('U', end=' ')
      print()

  def create_cells_from_map(self, map: Map) -> list[list[Cell]]:
    """
    Creates cells from a map.

    Args:
        map (Map): An instance of the Map class.

    Returns:
        list: A list of cells.
    """
    cells: list[list[Cell]] = []
    for row in range(map.get_rows()):
      cells.append([])
      for column in range(map.get_columns()):
        terrain: Optional[Terrain] = self.__terrain_repository.get_by_code(map.get_cell(row, column))
        if terrain is None:
          raise ValueError(f"Terrain with code {map.get_cell(row, column)} not found.")
        cells[row].append(Cell(terrain, row, column))
    return cells

  def create_environment_from_map(self, map: Map) -> Environment:
    """
    Creates an environment from a map.

    Args:
        map (Map): An instance of the Map class.

    Returns:
        Environment: An instance of the Environment class.
    """
    cells: list[list[Cell]] = self.create_cells_from_map(map)
    discovered_map: list[list[bool]] = [[False for _ in range(map.get_rows())] for _ in range(map.get_columns())]
    return Environment([], discovered_map, cells, map.get_rows(), map.get_columns())
