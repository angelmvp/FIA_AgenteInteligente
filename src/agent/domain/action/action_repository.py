from typing import Optional

from src.agent.domain.action.action import Action


class ActionRepository:
  """
  A repository for managing Action objects.

  Attributes:
    __actions (dict[str, Action]): A dictionary to store actions with their identifiers as keys.
  """

  def __init__(self):
    """
    Initializes an ActionRepository instance.
    """
    self.__actions: dict[str, Action] = {}

  def add_action(self, action: Action):
    """
    Adds an action to the repository.

    Args:
      action (Action): The action to add.
    """
    self.__actions[action.get_identifier()] = action

  def get_action(self, identifier: str) -> Optional[Action]:
    """
    Retrieves an action by its identifier.

    Args:
      identifier (str): The identifier of the action to retrieve.

    Returns:
      Optional[Action]: The action with the given identifier, or None if not found.
    """
    return self.__actions.get(identifier)

  def get_actions(self) -> list[Action]:
    """
    Retrieves all actions in the repository.

    Returns:
      list[Action]: A list of all actions.
    """
    return list(self.__actions.values())
