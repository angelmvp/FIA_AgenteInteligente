import flet

from ui.view.view_ui import ViewUi


class ViewUiService:
  def __init__(self, page: flet.Page):
    self.__page: flet.Page = page
    self.__views: dict[str, ViewUi] = {}

  def register(self, view: ViewUi) -> None:
    self.__views[view.get_identifier()] = view

  def create_control(self, identifier: str) -> list[flet.Control]:
    if identifier in self.__views:
      view_instance: ViewUi = self.__views[identifier]
      return view_instance.create_control()
    else:
      raise ValueError(f"View '{identifier}' not registered.")

  def navigate_to(self, identifier: str) -> None:
    if identifier in self.__views:
      view_instance: ViewUi = self.__views[identifier]
      view_instance.render(self.__page)
    else:
      raise ValueError(f"View '{identifier}' not registered.")

  def close(self) -> None:
    self.__page.window.close()
