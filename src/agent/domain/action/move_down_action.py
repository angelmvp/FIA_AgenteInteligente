from typing import Optional

from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Direction, Agent


class MoveDownAction(MoveAction):
  IDENTIFIER: str = 'move_down'

  def __init__(self) -> None:
    super().__init__(MoveDownAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    return MoveActionNewCoordinates(0, steps, Direction.DOWN)
