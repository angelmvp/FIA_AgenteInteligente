from typing import Optional

from enum import Enum

from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.known_cell import KnownCell
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration


class Direction(Enum):
  """
  Enum representing possible movement directions.
  """
  UP = 'up'
  DOWN = 'down'
  LEFT = 'left'
  RIGHT = 'right'

  def turn_left(self) -> 'Direction':
    """
    Returns the direction after turning left.

    Returns:
      Direction: The new direction.
    """
    if self == Direction.UP:
      return Direction.LEFT
    if self == Direction.DOWN:
      return Direction.RIGHT
    if self == Direction.LEFT:
      return Direction.DOWN
    if self == Direction.RIGHT:
      return Direction.UP

  def turn_right(self) -> 'Direction':
    """
    Returns the direction after turning right.

    Returns:
      Direction: The new direction.
    """
    if self == Direction.UP:
      return Direction.RIGHT
    if self == Direction.DOWN:
      return Direction.LEFT
    if self == Direction.LEFT:
      return Direction.UP
    if self == Direction.RIGHT:
      return Direction.DOWN


class Agent:
  """
  Represents an agent in the environment.

  Attributes:
    __accumulated_movement_cost (int): The accumulated cost of the agent.
    __actions (dict[str, ActionConfiguration]): The list of actions the agent can perform.
    __direction (Optional[Direction]): The direction the agent is facing.
    __known_map (list[list[KnownCell]]): The map of known cells.
    __name (str): The name of the agent.
    __sensors (dict[str, SensorConfiguration]): The list of sensors the agent has.
    __total_steps (int): The total number of steps the agent has taken.
    __x (int): The x-coordinate of the agent's position.
    __y (int): The y-coordinate of the agent's position.
  """

  def __init__(self, accumulated_movement_cost: int, actions: dict[str, ActionConfiguration], direction: Optional[Direction], known_map: list[list[Optional[KnownCell]]], name: str, sensors: dict[str, SensorConfiguration], total_steps: int, x: int, y: int):
    """
    Initializes an Agent instance.

    Args:
      accumulated_movement_cost (int): The accumulated cost of the agent.
      actions (dict[str, ActionConfiguration]): The list of actions the agent can perform.
      direction (Optional[Direction]): The direction the agent is facing.
      known_map (list[list[Optional[KnownCell]]]): The map of known cells.
      name (str): The name of the agent.
      sensors (dict[str, SensorConfiguration]): The list of sensors the agent has.
      total_steps (int): The total number of steps the agent has taken.
      x (int): The x-coordinate of the agent's position.
      y (int): The y-coordinate of the agent's position.
    """
    self.__accumulated_movement_cost: int = accumulated_movement_cost
    self.__actions: dict[str, ActionConfiguration] = actions
    self.__direction: Optional[Direction] = direction
    self.__known_map: list[list[KnownCell]] = known_map
    self.__name: str = name
    self.__sensors: dict[str, SensorConfiguration] = sensors
    self.__total_steps: int = total_steps
    self.__x: int = x
    self.__y: int = y

  def get_name(self) -> str:
    """
    Returns the name of the agent.

    Returns:
      str: The name.
    """
    return self.__name

  def add_action(self, action: ActionConfiguration) -> None:
    """
    Adds an action to the agent.

    Args:
      action (ActionConfiguration): The action to be added.
    """
    self.__actions[action.get_identifier()] = action

  def get_action(self, identifier: str) -> Optional[ActionConfiguration]:
    """
    Returns the action with the given identifier.

    Args:
      identifier (str): The identifier of the action.

    Returns:
      Optional[ActionConfiguration]: The action, or None if not found.
    """
    return self.__actions.get(identifier, None)

  def add_sensor(self, sensor: SensorConfiguration) -> None:
    """
    Adds a sensor to the agent.

    Args:
      sensor (SensorConfiguration): The sensor to be added.
    """
    self.__sensors[sensor.get_identifier()] = sensor

  def get_sensor(self, identifier: str) -> Optional[SensorConfiguration]:
    """
    Returns the sensor with the given identifier.

    Args:
      identifier (str): The identifier of the sensor.

    Returns:
      Optional[SensorConfiguration]: The sensor, or None if not found.
    """
    return self.__sensors.get(identifier, None)

  def set_known(self, x: int, y: int) -> None:
    """
    Updates the known map with the cell at the given position.

    Args:
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.
    """
    self.__known_map[x][y] = KnownCell([])

  def add_flag(self, x: int, y: int, flag: str) -> bool:
    """
    Adds a flag to a cell.

    Args:
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.
      flag (str): The flag to be added.

    Returns:
      bool: True if the flag was added, False if it was already present.
    """
    if not self.is_known(x, y):
      return False
    return self.__known_map[x][y].add_flag(flag)

  def is_known(self, x: int, y: int) -> bool:
    """
    Checks if a cell is known.

    Args:
      x (int): The x-coordinate of the cell.
      y (int): The y-coordinate of the cell.

    Returns:
      bool: True if the cell is known, False if it is not.
    """
    if x < 0 or x >= len(self.__known_map):
      return False
    return self.__known_map[x][y] is not None

  def update_position(self, x: int, y: int) -> None:
    """
    Updates the agent's position.

    Args:
      x (int): The new x-coordinate.
      y (int): The new y-coordinate.
    """
    self.__x = x
    self.__y = y

  def get_x(self) -> int:
    """
    Returns the x-coordinate of the agent's position.

    Returns:
      int: The x-coordinate.
    """
    return self.__x

  def get_y(self) -> int:
    """
    Returns the y-coordinate of the agent's position.

    Returns:
      int: The y-coordinate.
    """
    return self.__y

  def get_direction(self) -> Optional[Direction]:
    """
    Returns the direction the agent is facing.

    Returns:
      Optional[Direction]: The direction.
    """
    return self.__direction

  def set_direction(self, direction: Optional[Direction]) -> None:
    """
    Sets the direction the agent is facing.

    Args:
      direction (Optional[Direction]): The new direction.
    """
    self.__direction = direction

  def get_accumulated_movement_cost(self) -> int:
    """
    Returns the accumulated movement cost of the agent.

    Returns:
      int: The accumulated movement cost.
    """
    return self.__accumulated_movement_cost

  def increase_accumulated_movement_cost(self, cost: int) -> None:
    """
    Increases the accumulated movement cost of the agent.

    Args:
      cost (int): The cost to be added.
    """
    self.__accumulated_movement_cost += cost

  def get_total_steps(self) -> int:
    """
    Returns the total number of steps the agent has taken.

    Returns:
      int: The total number of steps.
    """
    return self.__total_steps

  def increase_total_steps(self) -> None:
    """
    Increases the total number of steps the agent has taken.
    """
    self.__total_steps += 1
