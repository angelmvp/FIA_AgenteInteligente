from typing import Optional

from src.agent.domain.action.action import ActionResult
from src.agent.domain.action.agent_action import ActionConfiguration
from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent
from src.environment.domain.environment import Environment


class MoveUpAction(MoveAction):
  IDENTIFIER: str = 'move_up'

  def __init__(self) -> None:
    super().__init__(MoveUpAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    return MoveActionNewCoordinates(0, -steps, Direction.UP)
