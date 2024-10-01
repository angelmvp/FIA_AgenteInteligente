from typing import Optional
from src.agent.domain.action.move_action import MoveAction, MoveActionNewCoordinates
from src.agent.domain.agent import Agent, Direction


class MoveForwardAction(MoveAction):
  IDENTIFIER: str = 'move_forward'

  def __init__(self) -> None:
    super().__init__(MoveForwardAction.IDENTIFIER)

  def get_new_coordinates(self, agent: Agent, steps: int) -> Optional[MoveActionNewCoordinates]:
    direction: Optional[Direction] = agent.get_direction()
    if direction is None:
      return None

    if direction == Direction.UP:
      return MoveActionNewCoordinates(0, -steps, direction)
    elif direction == Direction.DOWN:
      return MoveActionNewCoordinates(0, steps, direction)
    elif direction == Direction.LEFT:
      return MoveActionNewCoordinates(-steps, 0, direction)
    elif direction == Direction.RIGHT:
      return MoveActionNewCoordinates(steps, 0, direction)
    else:
      return None
