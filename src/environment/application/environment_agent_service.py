from abc import ABC
from enum import Enum
from os import environ
from typing import Optional

from src.agent.domain.action.action import Action, ActionResult
from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.agent_action import ActionConfiguration
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.sensor import Sensor, SensorResult
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor_repository import SensorRepository
from src.environment.domain.environment import Environment


class ResultCode(Enum):
  SUCCESS = 1
  NOT_FOUND_IN_AGENT = 2
  NOT_FOUND_IN_REPOSITORY = 3

class Result(ABC):
  def __init__(self, result_code: ResultCode):
    self.result_code = result_code

  def get_code(self) -> ResultCode:
    return self.result_code

class ExecuteActionResult(Result):
  def __init__(self, result_code: ResultCode, action_result: Optional[ActionResult]):
    super().__init__(result_code)
    self.__action_result = action_result

  def get_action_result(self) -> Optional[ActionResult]:
    return self.__action_result

class ExecuteSensorResult(Result):
  def __init__(self, result_code: ResultCode, sensor_result: Optional[SensorResult]):
    super().__init__(result_code)
    self.__sensor_result = sensor_result

  def get_sensor_result(self) -> Optional[SensorResult]:
    return self.__sensor_result


class EnvironmentAgentService:
  def __init__(self, action_repository: ActionRepository, sensor_repository: SensorRepository):
    self.__action_repository = action_repository
    self.__sensor_repository = sensor_repository

  def execute_action(self, agent: Agent, environment: Environment, action_identifier: str) -> ExecuteActionResult:
    """
    Executes an action for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the action.
      environment (Environment): The environment in which the agent will execute the action.
      action_identifier (str): The identifier of the action to be executed.
    """
    action_configuration: Optional[ActionConfiguration] = agent.get_action(action_identifier)
    if action_configuration is None:
      return ExecuteActionResult(ResultCode.NOT_FOUND_IN_AGENT, None)
    action: Action = self.__action_repository.get_action(action_identifier)
    if action is None:
      return ExecuteActionResult(ResultCode.NOT_FOUND_IN_REPOSITORY, None)
    action_result: ActionResult = action.execute(agent, action_configuration, environment)
    return ExecuteActionResult(ResultCode.SUCCESS, action_result)

  def execute_sensor(self, agent: Agent, environment: Environment, sensor_identifier: str) -> ExecuteSensorResult:
    """
    Executes a sensor for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the sensor.
      environment (Environment): The environment in which the agent will execute the sensor.
      sensor_identifier (str): The identifier of the sensor to be executed.
    """
    sensor_configuration: Optional[SensorConfiguration] = agent.get_sensor(sensor_identifier)
    if sensor_configuration is None:
      return ExecuteSensorResult(ResultCode.NOT_FOUND_IN_AGENT, None)
    sensor: Sensor = self.__sensor_repository.get_sensor(sensor_identifier)
    if sensor is None:
      return ExecuteSensorResult(ResultCode.NOT_FOUND_IN_REPOSITORY, None)
    sensor_result: SensorResult = sensor.detect(agent, sensor_configuration, environment)
    return ExecuteSensorResult(ResultCode.SUCCESS, sensor_result)
