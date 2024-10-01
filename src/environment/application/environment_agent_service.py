from enum import Enum
from os import environ

from src.agent.domain.action.action import Action
from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.agent_action import ActionConfiguration
from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment

class ExecuteActionResult(Enum):
  SUCCESS = 1
  NOT_FOUND_IN_AGENT = 2
  NOT_FOUND_IN_REPOSITORY = 3

class EnvironmentAgentService:
  def __init__(self, action_repository: ActionRepository):
    self.__action_repository = action_repository

  def execute_action(self, agent: Agent, environment: Environment, action_identifier: str) -> ExecuteActionResult:
    """
    Executes an action for an agent in an environment.

    Args:
      agent (Agent): The agent that will execute the action.
      environment (Environment): The environment in which the agent will execute the action.
      action_identifier (str): The identifier of the action to be executed.
    """
    agent_action: ActionConfiguration = agent.get_action(action_identifier)
    if agent_action is None:
      return ExecuteActionResult.NOT_FOUND_IN_AGENT
    action: Action = self.__action_repository.get_action(action_identifier)
    if action is None:
      return ExecuteActionResult.NOT_FOUND_IN_REPOSITORY
    action.execute(agent, agent_action, environment)
