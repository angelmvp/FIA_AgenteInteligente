import pygame
import pygame_gui
from pygame_gui.core import ObjectID

class View:
    def __init__(self, window_surface, manager):
        self.window_surface = window_surface
        self.manager = manager

    def process_events(self, event):
        pass

    def update(self, time_delta):
        pass

    def draw(self):
        pass

class MapCreation(View):
    def __init__(self, window_surface, manager):
        self.window_surface = window_surface
        self.manager = manager
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        background = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        background.fill(pygame.Color('#FFFFFF'))  # Fondo blanco para coincidir con la imagen
        super().__init__(window_surface, manager)
        self.rows = None
        self.columns = None
        self.action=None
        self.setup_ui()

    def setup_ui(self):
        self.TITLE_HEIGHT = 100
        self.BUTTON_WIDTH = 150
        self.BUTTON_HEIGHT = 50

        # Título
        title_rect = pygame.Rect(0, 50, self.SCREEN_WIDTH, 50)
        self.title_label = pygame_gui.elements.UILabel(
            relative_rect=title_rect,
            text='Tamaño del mapa',
            manager=self.manager,
            object_id=ObjectID(class_id='@title')
        )


        label_rows_rect = pygame.Rect(self.SCREEN_WIDTH // 4 - 50, 200, 100, 50)
        self.label_rows = pygame_gui.elements.UILabel(
            relative_rect=label_rows_rect,
            text='Filas',
            manager=self.manager
        )

        input_rows_rect = pygame.Rect(self.SCREEN_WIDTH // 4 + 50, 200, 100, 50)
        self.input_rows = pygame_gui.elements.UITextEntryLine(
            relative_rect=input_rows_rect,
            manager=self.manager
        )

        # Etiqueta de self.columns y campo de entrada
        label_columns_rect = pygame.Rect(3 * self.SCREEN_WIDTH // 4 - 150, 200, 100, 50)
        self.label_columns = pygame_gui.elements.UILabel(
            relative_rect=label_columns_rect,
            text='Columnas',
            manager=self.manager
        )

        input_columns_rect = pygame.Rect(3 * self.SCREEN_WIDTH // 4 - 50, 200, 100, 50)
        self.input_columns = pygame_gui.elements.UITextEntryLine(
            relative_rect=input_columns_rect,
            manager=self.manager
        )

        button_back_rect = pygame.Rect(self.SCREEN_WIDTH // 4 - self.BUTTON_WIDTH // 2, 400, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.button_back = pygame_gui.elements.UIButton(
            relative_rect=button_back_rect,
            text='Regresar',
            manager=self.manager
        )

        button_next_rect = pygame.Rect(3 * self.SCREEN_WIDTH // 4 - self.BUTTON_WIDTH // 2, 400, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.button_next = pygame_gui.elements.UIButton(
            relative_rect=button_next_rect,
            text='Siguiente',
            manager=self.manager
        )

    def process_events(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button_back:
                self.action="back"
                print('Retroceder')
            elif event.ui_element == self.button_next:
                self.action="advance"
                self.rows = self.input_rows.get_text()
                self.columns =  self.input_columns.get_text()
                if self.rows.isdigit() and self.columns.isdigit():
                    self.rows = int(self.rows)
                    self.columns = int(self.columns)

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self):
        self.window_surface.fill(pygame.Color('#000000'))  # Fondo blanco
        self.manager.draw_ui(self.window_surface)
        pygame.display.update()
    def get_action(self):
        if self.action is not None:
            self.clear_ui()  # Limpiar la interfaz
            return self.action  # Devuelve la acción
        return None
    def get_rows(self):
        return self.rows
    def get_columns(self):
        return self.columns
    def clear_ui(self):
        self.title_label.kill()
        self.label_rows.kill()
        self.input_rows.kill()
        self.label_columns.kill()
        self.input_columns.kill()
        self.button_back.kill()
        self.button_next.kill()

