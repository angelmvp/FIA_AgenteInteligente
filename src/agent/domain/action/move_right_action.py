from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveRightAction(MoveAction):
  IDENTIFIER: str = 'move_right'

  def __init__(self) -> None:
    super().__init__(MoveRightAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    return MoveActionNewCoordinates(steps, 0, Direction.RIGHT)
