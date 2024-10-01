from abc import abstractmethod
from enum import Enum

from src.agent.domain.agent import Agent, Direction
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.environment.domain.environment import Environment

class SensorResult(Enum):
  SUCCESS = 0
  UNKNOWN_CELL = 1
  OUT_OF_BOUNDS = 2
  HIT_OBSTACLE = 3

class Sensor:
  """
  Represents a sensor that detects the terrain type in the cells around the agent.

  Attributes:
    __identifier (str): The sensor identifier.
  """

  def __init__(self, identifier: str):
    """
    Initializes a Sensor instance.
    """
    self.__identifier = identifier

  def get_identifier(self) -> str:
    """
    Returns the sensor identifier.

    Returns:
      str: The sensor identifier.
    """
    return self.__identifier

  @abstractmethod
  def detect(self, agent: Agent, sensor_configuration: SensorConfiguration, environment: Environment) -> SensorResult:
    """
    Detects the terrain type in the cells around the agent, updating its individual knowledge and the global map of the environment.

    Args:
      agent (Agent): The agent that will detect the terrain type.
      sensor_configuration (SensorConfiguration): The specific sensor configuration for the agent.
      environment (Environment): The environment in which the agent operates.

    Returns:
      SensorResult: The result of the sensor detection.
    """
    raise NotImplementedError("This method should be implemented by the subclass.")
