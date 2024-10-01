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
        self.sensor=None
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

        # Contenedor para los botones y las etiquetas
        self.menu_container_img = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(100, self.TITLE_HEIGHT, self.SCREEN_WIDTH - self.PADDING_IMG,
                                       self.SCREEN_HEIGHT - self.TITLE_HEIGHT),
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_img'))
        self.sensor1_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.PADDING_IMG, self.PADDING_IMG,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.IMAGE_HEIGHT - self.PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor1_button')
        )

        self.sensor1_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.PADDING_IMG, self.IMAGE_HEIGHT,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.BUTTON_HEIGHT // 2),
            text='Celda enfrente',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@sensor_label')
        )

        # Sensor 2
        self.sensor2_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.SCREEN_WIDTH // 2, self.PADDING_IMG,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.IMAGE_HEIGHT - self.PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor2_button')
        )

        self.sensor2_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.SCREEN_WIDTH // 2, self.IMAGE_HEIGHT,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.BUTTON_HEIGHT // 2),
            text='4 celdas',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@sensor_label')
        )

        # Sensor 3
        self.sensor3_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.PADDING_IMG, (self.SCREEN_HEIGHT - self.TITLE_HEIGHT) // 2,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.IMAGE_HEIGHT - self.PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor3_button')
        )

        self.sensor3_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.PADDING_IMG, (self.SCREEN_HEIGHT - self.TITLE_HEIGHT) // 2 + self.IMAGE_HEIGHT,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.BUTTON_HEIGHT // 2),
            text='Sensor 3x3',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@sensor_label')
        )

        # Sensor 4
        self.sensor4_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT - self.TITLE_HEIGHT) // 2,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.IMAGE_HEIGHT - self.PADDING_IMG),
            text='',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor4_button')
        )

        self.sensor4_label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(self.SCREEN_WIDTH // 2, (self.SCREEN_HEIGHT - self.TITLE_HEIGHT) // 2 + self.IMAGE_HEIGHT,
                                       self.IMAGE_WIDTH - self.PADDING_IMG,
                                       self.BUTTON_HEIGHT // 2),
            text='Otro Sensor',
            manager=self.manager,
            container=self.menu_container_img,
            object_id=ObjectID(class_id='@sensor_label')
        )

    def process_events(self, event):
        advance=False
        back=False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            print("dalkfkal")
            if event.ui_element ==self.button_back:
                print('Retroceder')
                back=True
            elif event.ui_element == self.sensor1_button:
                print('Sensor 1 seleccionado')
                self.sensor="sensor1"
                advance=True
            elif event.ui_element == self.sensor2_button:
                print('Sensor 2 seleccionado')
                self.sensor="sensor2"
                advance=True
            elif event.ui_element == self.sensor3_button:
                print('Sensor 3 seleccionado')
                self.sensor="sensor3"
                advance=True
            elif event.ui_element == self.sensor4_button:
                print('Sensor 4 seleccionado')
                self.sensor="sensor4"
                advance=True
        # if advance==True:
        #     return self.sensor
        # if back==True:
        #     return "back"
     
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
        self.sensor1_button.kill()
        self.sensor1_label.kill()
        self.sensor2_button.kill()
        self.sensor2_label.kill()
        self.sensor3_button.kill()
        self.sensor3_label.kill()
        self.sensor4_button.kill()
        self.sensor4_label.kill()
