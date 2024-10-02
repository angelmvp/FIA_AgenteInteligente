from typing import Optional

import flet

from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.cell.cell import Cell
from ui.ui_constants import UiConstants
from ui.view.view_ui import ViewUi
from ui.view.view_ui_constants import ViewUiConstants


class PlayAgentPositionSelectionViewUi(ViewUi):
  def __init__(self, environment_service: EnvironmentService):
    super().__init__(ViewUiConstants.PLAY_AGENT_POSITION_SELECTION_SCREEN_IDENTIFIER)
    self.__environment_service: EnvironmentService = environment_service
    self.grid_view: Optional[flet.Column] = None
    self.cell_size = 25
    self.spacing = 5
    self.visible_columns = 25
    self.visible_rows = 25
    self.start_row = 0
    self.start_col = 0

  def generate_visible_cells(self, start_row: int, start_col: int):
    grid_items: list[flet.Row] = []
    for row in range(start_row, start_row + self.visible_rows):
      row_containers: list[flet.Container] = []
      for col in range(start_col, start_col + self.visible_columns):
        cell: Optional[Cell] = self.__environment_service.get_environment().get_cell(row, col)
        if cell is None:
          continue
        row_containers.append(
          flet.Container(
            width=self.cell_size,
            height=self.cell_size,
            bgcolor=cell.get_terrain().get_color(),
            on_click=lambda e, selected_row=row, selected_col=col: print(f"Selected cell: {selected_row}, {selected_col}")
          )
        )
      grid_items.append(
        flet.Row(
          controls=row_containers,
          alignment=flet.MainAxisAlignment.CENTER,
          spacing=self.spacing,
          run_spacing=self.spacing
        )
      )
    return grid_items

  def create_control(self) -> list[flet.Control]:
    if self.__environment_service.get_environment() is None:
      return [
        flet.Text("No se ha seleccionado un mapa", style=UiConstants.TITLE_TEXT_STYLE)
      ]

    # Tamaño de la vista
    view_width = self.visible_columns * self.cell_size + ((self.visible_columns - 1) * (self.spacing * 2))
    view_height = self.visible_rows * self.cell_size + ((self.visible_rows - 1) * (self.spacing * 2))

    print(f"Visible columns: {self.visible_columns} Visible rows: {self.visible_rows} View width: {view_width} View height: {view_height}")

    # Inicializar las celdas visibles
    grid_items: list[flet.Row] = self.generate_visible_cells(self.start_row, self.start_col)
    self.grid_view = flet.Column(
      width=view_width,
      height=view_height,
      controls=grid_items,
      spacing=self.spacing,
      run_spacing=self.spacing
    )

    # Crear botones de navegación
    up_button = flet.ElevatedButton("⬆", style=UiConstants.BUTTON_STYLE, on_click=self.on_up_click)
    down_button = flet.ElevatedButton("⬇", style=UiConstants.BUTTON_STYLE, on_click=self.on_down_click)
    left_button = flet.ElevatedButton("⬅", style=UiConstants.BUTTON_STYLE, on_click=self.on_left_click)
    right_button = flet.ElevatedButton("➡", style=UiConstants.BUTTON_STYLE, on_click=self.on_right_click)

    navigation_controls = flet.Row(
      controls=[
        left_button,
        flet.Column(controls=[up_button, down_button]),
        right_button
      ],
      alignment=flet.MainAxisAlignment.CENTER
    )

    return [
      self.grid_view,
      navigation_controls
    ]

  def update_grid_view(self):
    new_grid_items = self.generate_visible_cells(self.start_row, self.start_col)
    self.grid_view.controls = new_grid_items
    self.grid_view.update()

  def on_up_click(self, e):
    if self.start_row > 0:
      self.start_row -= 1
      self.update_grid_view()

  def on_down_click(self, e):
    if self.start_row + self.visible_rows < self.__environment_service.get_environment().get_rows():
      self.start_row += 1
      self.update_grid_view()

  def on_left_click(self, e):
    if self.start_col > 0:
      self.start_col -= 1
      self.update_grid_view()

  def on_right_click(self, e):
    if self.start_col + self.visible_columns < self.__environment_service.get_environment().get_columns():
      self.start_col += 1
      self.update_grid_view()
