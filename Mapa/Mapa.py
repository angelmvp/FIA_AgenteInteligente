import pygame
import pygame_gui
from pygame_gui.core import ObjectID

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
TITLE_HEIGHT = 100
IMAGE_WIDTH = SCREEN_WIDTH // 4
IMAGE_HEIGHT = IMAGE_WIDTH
PADDING_IMG = 10
BUTTON_WIDTH = 150
BUTTON_HEIGHT = TITLE_HEIGHT // 2
pygame.init()
pygame.display.set_caption('Agent Menu')

clock = pygame.time.Clock()

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

class MapGame(View):
    def __init__(self, window_surface, manager):
        print("Vista mapa juego")
        self.running = True
        self.window_surface = window_surface
        self.manager = manager
        self.action = None
        self.setup_ui()

    def setup_ui(self):
        # Panel de encabezado
        panel_header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, TITLE_HEIGHT)
        self.panel_header = pygame_gui.elements.UIPanel(
            relative_rect=panel_header_rect,
            manager=self.manager,
            object_id=ObjectID(class_id='@panel_header')
        )

        # Botón de regresar
        button_back_rect = pygame.Rect(20, TITLE_HEIGHT // 4, BUTTON_WIDTH, BUTTON_HEIGHT)
        self.button_back = pygame_gui.elements.UIButton(
            relative_rect=button_back_rect,
            text="Regresar",
            manager=self.manager,
            container=self.panel_header,
            object_id=ObjectID(class_id='@buttons_navigation')
        )

        # Título
        label_title_rect = pygame.Rect(SCREEN_WIDTH // 4, TITLE_HEIGHT // 4, SCREEN_WIDTH // 2, TITLE_HEIGHT // 2)
        self.label_title_map = pygame_gui.elements.UILabel(
            relative_rect=label_title_rect,
            text='MAPA PRINCIPAL JUEGO JUEGO',
            manager=self.manager,
            container=self.panel_header,
            object_id=ObjectID(class_id='@title', object_id='#title_map_modified')
        )

        # Contenedor para los botones y las etiquetas
        self.menu_container_img = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(100, TITLE_HEIGHT, SCREEN_WIDTH - PADDING_IMG, SCREEN_HEIGHT - TITLE_HEIGHT),
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_img')
        )

        # Botones
        self.menu_bottom = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PADDING_IMG, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='RegresaMenu',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#nada')
        )

        self.agent_selection_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='Seleccionar Otro Agente',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#agent_button')
        )

        self.actions_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PADDING_IMG, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='Ajustar Acciones',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#action_button')
        )

        self.sensors_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(SCREEN_WIDTH // 2, (SCREEN_HEIGHT - TITLE_HEIGHT) // 2, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='Ajustar Sensores',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor_button')
        )

    def process_events(self, event):
        advance = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button_back:
                print('Retroceder al menú principal')
                advance = True
                self.sensor = "back"
            elif event.ui_element == self.menu_bottom:
                print('Regresa al menú')
                advance = True
                self.action = "menu"
            elif event.ui_element == self.agent_selection_button:
                print('Seleccionar otro agente')
                advance = True
                self.action = "agent_selection"
            elif event.ui_element == self.actions_button:
                print('Ajustar acciones')
                advance = True
                self.action = "actions"
            elif event.ui_element == self.sensors_button:
                print('Ajustar sensores')
                advance = True
                self.action = "sensors"
        
        if advance:
            return self.action

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self):
        self.window_surface.fill(pygame.Color('#000000'))
        self.manager.draw_ui(self.window_surface)
        pygame.display.update()

    def get_action(self):
        if self.action:
            self.clear_ui()
            return self.action

    def clear_ui(self):
        self.panel_header.kill()
        self.button_back.kill()
        self.label_title_map.kill()
        self.menu_container_img.kill()
        self.menu_bottom.kill()
        self.agent_selection_button.kill()
        self.actions_button.kill()
        self.sensors_button.kill()

