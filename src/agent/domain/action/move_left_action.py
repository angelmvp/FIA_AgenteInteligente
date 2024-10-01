from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveLeftAction(MoveAction):
  IDENTIFIER: str = 'move_left'

  def __init__(self) -> None:
    super().__init__(MoveLeftAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    return MoveActionNewCoordinates(-steps, 0, Direction.LEFT)
