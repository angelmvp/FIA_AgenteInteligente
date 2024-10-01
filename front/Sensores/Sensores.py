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

class SeleccionarSensor(View):
    def __init__(self, window_surface, manager):
        print("nueva seleccion Sensores")
        self.window_surface = window_surface
        self.manager = manager
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 700
        background = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        background.fill(pygame.Color('#000000'))
        super().__init__(window_surface, manager)
        self.clock = pygame.time.Clock()
        self.sensor = None
        self.setup_ui()

    def setup_ui(self):
        self.TITLE_HEIGHT = 100
        self.IMAGE_WIDTH = self.SCREEN_WIDTH // 4
        self.IMAGE_HEIGHT = self.IMAGE_WIDTH
        self.PADDING_IMG = 10
        self.BUTTON_WIDTH = 150
        self.BUTTON_HEIGHT = self.TITLE_HEIGHT // 2

        self.background = pygame.Surface((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.background.fill(pygame.Color('#000000'))

        # Panel del encabezado
        panel_header_rect = pygame.Rect(0, 0, self.SCREEN_WIDTH, self.TITLE_HEIGHT)
        self.panel_header = pygame_gui.elements.UIPanel(relative_rect=panel_header_rect,
                                                        manager=self.manager,
                                                        object_id=ObjectID(class_id='@panel_header'))

        # Botón Regresar
        button_back_rect = pygame.Rect(20, self.TITLE_HEIGHT // 4, self.BUTTON_WIDTH, self.BUTTON_HEIGHT)
        self.button_back = pygame_gui.elements.UIButton(relative_rect=button_back_rect,
                                                        text="Regresar",
                                                        manager=self.manager,
                                                        container=self.panel_header,
                                                        object_id=ObjectID(class_id='@buttons_navigation'))

        # Título
        label_title_rect = pygame.Rect(self.SCREEN_WIDTH // 4, self.TITLE_HEIGHT // 4,
                                       self.SCREEN_WIDTH // 2, self.TITLE_HEIGHT // 2)
        self.label_title_map = pygame_gui.elements.UILabel(relative_rect=label_title_rect,
                                                           text='SELECCIONAR TIPO DE SENSOR',
                                                           manager=self.manager,
                                                           container=self.panel_header,
                                                           object_id=ObjectID(class_id='@title', object_id='#title_map_modified'))

        # Contenedor horizontal con scroll para los botones de los sensores
        panel_width = 1200  # Ancho del panel más grande que la pantalla
        panel_height = self.IMAGE_HEIGHT + self.BUTTON_HEIGHT + self.PADDING_IMG * 2
        panel_rect = pygame.Rect(50, self.SCREEN_HEIGHT // 2 - panel_height // 2, self.SCREEN_WIDTH - 100, panel_height)

        self.menu_container_img = pygame_gui.elements.UIPanel(
            relative_rect=panel_rect,
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_img')
        )

        # Panel de contenido que será desplazado
        content_panel_rect = pygame.Rect(0, 0, panel_width, panel_height)
        self.content_panel = pygame_gui.elements.UIPanel(
            relative_rect=content_panel_rect,
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@content_panel')
        )

        # Botones dentro del contenedor horizontal
        self.sensor1_button=self.create_sensor_button(0, 'Celda enfrente', '#sensor1_button')
        self.sensor2_button=self.create_sensor_button(1, '4 celdas', '#sensor2_button')
        self.sensor3_button=self.create_sensor_button(2, 'Sensor 3x3', '#sensor3_button')
        self.sensor4_button=self.create_sensor_button(3, 'Otro Sensor', '#sensor4_button')

        # Barra de desplazamiento horizontal
        scroll_bar_width = panel_rect.width
        self.scroll_bar = pygame_gui.elements.UIHorizontalScrollBar(
            relative_rect=pygame.Rect(50, panel_rect.bottom + 10, scroll_bar_width, 20),
            manager=self.manager,
            visible_percentage=panel_rect.width / panel_width
        )

    def create_sensor_button(self, index, label_text, button_id):
        button_x = index * (self.IMAGE_WIDTH + self.PADDING_IMG)
        
        sensor_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(button_x, self.PADDING_IMG, self.IMAGE_WIDTH, self.IMAGE_HEIGHT),
            text='',
            manager=self.manager,
            container=self.content_panel,
            object_id=ObjectID(class_id='@img_button', object_id=button_id)
        )

        sensor_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(button_x, self.IMAGE_HEIGHT + self.PADDING_IMG, self.IMAGE_WIDTH, self.BUTTON_HEIGHT),
            text=label_text,
            manager=self.manager,
            container=self.content_panel,
            object_id=ObjectID(class_id='@sensor_label')
            
        )
        return sensor_button

    def process_events(self, event):
        advance = False
        back = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button_back:
                print('Retroceder')
                back = True
            elif event.ui_element == self.sensor1_button:
                print('Sensor 1 seleccionado')
                self.sensor = "sensor1"
                advance = True
            elif event.ui_element == self.sensor2_button:
                print('Sensor 2 seleccionado')
                self.sensor = "sensor2"
                advance = True
            elif event.ui_element == self.sensor3_button:
                print('Sensor 3 seleccionado')
                self.sensor = "sensor3"
                advance = True
            elif event.ui_element == self.sensor4_button:
                print('Sensor 4 seleccionado')
                self.sensor = "sensor4"
                advance = True

        # Sincronizar el scroll horizontal con el panel de contenido
        if event.type == pygame_gui.UI_HORIZONTAL_SCROLL_BAR_CHANGED:
            scroll_x = event.value
            self.content_panel.set_relative_position(pygame.math.Vector2(-scroll_x, 0))

    def update(self, time_delta):
        self.manager.update(time_delta)

    def draw(self):
        self.window_surface.fill(pygame.Color('#000000'))
        self.manager.draw_ui(self.window_surface)
        pygame.display.update()

    def get_sensor(self):
        if self.sensor is not None:
            self.clear_ui()
            print(self.sensor)
            return self.sensor

    def clear_ui(self):
        self.panel_header.kill()
        self.button_back.kill()
        self.label_title_map.kill()
        self.menu_container_img.kill()
        self.content_panel.kill()
        self.scroll_bar.kill()
