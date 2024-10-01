class KnownCell:
  def __init__(self, flags: list[str]):
    """
    Initializes a CellAgent instance.

    Args:
      flags (list[str]): The list of flags associated with the cell.
    """
    self.__flags: list[str] = flags

  def add_flag(self, flag: str) -> bool:
    """
    Adds a flag to the cell.

    Args:
        flag (str): The flag to be added.

    Returns:
        bool: True if the flag was added, False if it was already present.
    """
    if flag not in self.__flags:
      self.__flags.append(flag)
      return True
    return False

  def remove_flag(self, flag: str) -> bool:
    """
    Removes a flag from the cell.

    Args:
        flag (str): The flag to be removed.

    Returns:
        bool: True if the flag was removed, False if it was not present.
    """
    if flag in self.__flags:
      self.__flags.remove(flag)
      return True
    return False

  def has_flag(self, flag: str) -> bool:
    """
    Checks if the cell has a specific flag.

    Args:
        flag (str): The flag to check.

    Returns:
        bool: True if the flag is present, False otherwise.
    """
    return flag in self.__flags
