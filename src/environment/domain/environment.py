from typing import Optional

from src.agent.domain.agent import Agent
from src.environment.domain.cell.cell import Cell


class Environment:
  """
  Represents the environment in which agents operate.

  Attributes:
    __agents (list[Agent]): The list of agents in the environment.
    __discovered_map (list[list[bool]]): The map of discovered cells.
    __grid (list[list[Cell]]): The grid representing the environment.
    __rows (int): The number of rows in the environment.
    __columns (int): The number of columns in the environment.
  """

  def __init__(self, agents: list[Agent], discovered_map: list[list[bool]], grid: list[list[Cell]], rows: int, columns: int):
    """
    Initializes an Environment instance.

    Args:
      agents (list[Agent]): The list of agents in the environment.
      discovered_map (list[list[bool]]): The map of discovered cells.
      grid (list[list[Cell]]): The grid representing the environment.
      rows (int): The number of rows in the environment.
      columns (int): The number of columns in the environment
    """
    self.__agents: list[Agent] = agents
    self.__discovered_map: list[list[bool]] = discovered_map
    self.__grid: list[list[Cell]] = grid
    self.__rows: int = rows
    self.__columns: int = columns

  def add_agent(self, agent: Agent):
    """
    Adds an agent to the environment.

    Args:
      agent (Agent): The agent to be added.
    """
    self.__agents.append(agent)

  def get_cell(self, x: int, y: int) -> Optional[Cell]:
    """
    Returns the state of the terrain at a specific position.

    Args:
      x (int): The x-coordinate of the position.
      y (int): The y-coordinate of the position.

    Returns:
      Cell: The cell at the specified position.
    """
    if x < 0 or x >= self.__rows or y < 0 or y >= self.__columns:
      return None
    return self.__grid[x][y]

  def update_discovered_map(self, x: int, y: int, value: bool):
    """
    Updates the discovered map at a specific position.

    Args:
      x (int): The x-coordinate of the position to update.
      y (int): The y-coordinate of the position to update.
      value (bool): The new value for the position.
    """
    self.__discovered_map[x][y] = value

  def get_discovered_map(self) -> list[list[bool]]:
    """
    Returns the discovered map.

    Returns:
      list[list[bool]]: The discovered map.
    """
    return self.__discovered_map

  def is_discovered(self, x: int, y: int) -> bool:
    """
    Checks if a cell has been discovered.

    Args:
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.

    Returns:
      bool: True if the cell has been discovered, False otherwise.
    """
    return self.__discovered_map[x][y]

  def update_state(self, x: int, y: int, new_value: Cell):
    """
    Changes the state of the environment at a position and updates both the global and agents' maps.

    Args:
      x (int): The x-coordinate of the position to update.
      y (int): The y-coordinate of the position to update.
      new_value (Cell): The new value for the position.
    """
    self.__grid[x][y] = new_value

  def is_obstacle_for(self, agent: Agent, x: int, y: int) -> Optional[bool]:
    """
    Checks if a cell is an obstacle for an agent.

    Args:
      agent (Agent): The agent to check the cell for.
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.

    Returns:
      bool: True if the cell is an obstacle for the agent, False otherwise.
    """
    cell: Optional[Cell] = self.get_cell(x, y)
    if cell is None:
      return None
    return cell.get_movement_cost_for(agent.get_name()) is None

  def get_rows(self) -> int:
    """
    Returns the number of rows in the environment.

    Returns:
      int: The number of rows.
    """
    return self.__rows

  def get_columns(self) -> int:
    """
    Returns the number of columns in the environment.

    Returns:
      int: The number of columns.
    """
    return self.__columns
