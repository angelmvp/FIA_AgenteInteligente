class ActionConfiguration:
  """
  Represents an action that an agent can perform.

  Attributes:
    __identifier (str): The identifier of the action.
    __properties (dict[str, any]): The properties of the action.
  """

  def __init__(self, identifier: str, properties: dict[str, any]):
    """
    Initializes an AgentAction instance.

    Args:
      identifier (str): The identifier of the action.
      properties (dict[str, any]): The properties of the action.
    """
    self.__identifier: str = identifier
    self.__properties: dict[str, any] = properties

  def get_identifier(self) -> str:
    """
    Returns the identifier of the action.

    Returns:
      str: The identifier.
    """
    return self.__identifier

  def get_property(self, key: str) -> any:
    """
    Returns the property with the specified key.

    Args:
      key (str): The key of the property.
    """
    return self.__properties[key]
