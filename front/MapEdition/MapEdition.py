import pygame
import pygame_gui
from pygame_gui.core import ObjectID

SCREEN_WIDTH=1000
SCREEN_HEIGHT=700
MENU_WIDTH=300
TITLE_HEIGHT=100
IMAGE_WIDTH=MENU_WIDTH//2
IMAGE_HEIGHT=IMAGE_WIDTH
PADDING_IMG=10
BUTTON_WIDTH=150
BUTTON_HEIGHT=TITLE_HEIGHT//2
MENU_INSTRUCTIONS_HEIGHT = (SCREEN_HEIGHT-TITLE_HEIGHT)//2
LABEL_HEIGHT=35

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

class MapEdition(View):
    def __init__(self, window_surface, manager,map_data,rows,columns):
        print("Vista edicion juego")
        self.map_data=map_data
        self.window_surface = window_surface
        self.manager = manager
        background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        background.fill(pygame.Color('#000000'))
        super().__init__(window_surface, manager)
        self.action = None
        self.name_new_map=None
        self.rows=rows
        self.columns=columns
        print(self.rows)
        print(self.columns)
        self.setup_ui()

    def setup_ui(self):
        # Panel de encabezado
        panel_header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, TITLE_HEIGHT)
        self.panel_header = pygame_gui.elements.UIPanel(
            relative_rect=panel_header_rect,
            manager=self.manager,
            object_id=ObjectID(class_id='@panel_header')
        )


        # Título
        label_title_rect = pygame.Rect(SCREEN_WIDTH // 4, TITLE_HEIGHT // 4, SCREEN_WIDTH // 2, TITLE_HEIGHT // 2)
        self.label_title_map = pygame_gui.elements.UILabel(
            relative_rect=label_title_rect,
            text='MAPA EDICION EDICION EDICION JUEGO JUEGO',
            manager=self.manager,
            container=self.panel_header,
            object_id=ObjectID(class_id='@title', object_id='#title_map_modified')
        )
        rect_edition = pygame.Rect(
            SCREEN_WIDTH - MENU_WIDTH, 
            TITLE_HEIGHT, 
            MENU_WIDTH, 
            SCREEN_HEIGHT - MENU_INSTRUCTIONS_HEIGHT-TITLE_HEIGHT
        )
        
        self.menu_edition = pygame_gui.elements.UIPanel(
            relative_rect=rect_edition,
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_edition')
        )
        rect_label_celda_title = pygame.Rect(0, 0, MENU_WIDTH,LABEL_HEIGHT )
        self.label_celda_title = pygame_gui.elements.UILabel(relative_rect=rect_label_celda_title,text=('MODIFICACION DEL MAPA'),
            manager=self.manager,container=self.menu_edition,object_id=ObjectID(class_id='@label_info_title'))
        
        rect_label_terrain_type=pygame.Rect(0,LABEL_HEIGHT+5,MENU_WIDTH,LABEL_HEIGHT)
        self.label_terrain_type=pygame_gui.elements.UILabel(relative_rect=rect_label_terrain_type,text=('Terreno'),
            manager=self.manager,container=self.menu_edition,object_id=ObjectID(class_id='@label_info')) 

        rect_label_position=pygame.Rect(0,2*LABEL_HEIGHT+5,MENU_WIDTH,LABEL_HEIGHT)
        self.label_position=pygame_gui.elements.UILabel(relative_rect=rect_label_position,text=('Posicion'),
            manager=self.manager,container=self.menu_edition,object_id=ObjectID(class_id='@label_info_title'))
        




        # Contenedor para los botones y las etiquetas
        self.menu_buttons = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(SCREEN_WIDTH-MENU_WIDTH,
            TITLE_HEIGHT+MENU_INSTRUCTIONS_HEIGHT,
            MENU_WIDTH,
            SCREEN_HEIGHT-TITLE_HEIGHT-MENU_INSTRUCTIONS_HEIGHT),
            manager=self.manager,
            object_id=ObjectID(class_id='@menu_container_img')
        )

        # Botones
        self.menu_save = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(PADDING_IMG, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='RegresaMenu',
            manager=self.manager,
            container=self.menu_buttons,
            object_id=ObjectID(class_id='@img_button', object_id='#nada')
        )
        label_columns_rect = pygame.Rect(3 * SCREEN_WIDTH // 4 - 150, 200, 100, 50)
        self.label_columns = pygame_gui.elements.UILabel(
            relative_rect=label_columns_rect,
            text='Columnas',
            manager=self.manager
        )

        input_name_rect = pygame.Rect(30,30,MENU_WIDTH//3,LABEL_HEIGHT)
        self.input_name = pygame_gui.elements.UITextEntryLine(relative_rect=input_name_rect,
            container=self.menu_buttons,
            manager=self.manager
        )

        button_back_rect = pygame.Rect(0, 0,
                               IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG)
        self.button_back = pygame_gui.elements.UIButton(
            relative_rect=button_back_rect,
            text='Regresar',
            manager=self.manager,
            container=self.menu_buttons
        )


        self.save_map_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(MENU_WIDTH // 2, (SCREEN_HEIGHT - TITLE_HEIGHT - MENU_INSTRUCTIONS_HEIGHT) // 2,
                               IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
            text='Guardar Mapa ',
            manager=self.manager,
            container=self.menu_buttons,
            object_id=ObjectID(class_id='@img_button', object_id='#sensor_button')
        )

    def process_events(self, event):
        advance = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.button_back:
                print('Retroceder al menú principal')
                advance = True
                self.sensor = "back"
            elif event.ui_element == self.save_map_button:
                self.name_new_map=self.input_name.get_text()
                print('guardar')
                advance = True
                self.action = "save"        
        if advance:
            return self.action
    def draw_map(self):
        pass
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
        self.menu_buttons.kill()
        self.menu_save.kill()
        self.agent_selection_button.kill()
        self.actions_button.kill()
        self.sensors_button.kill()
        self.menu_edition.kill()
        # self.label_celda_title.kill()
        # self.label_terrain_type.kill()
        # self.label_cost.kill()
        # self.label_mark.kill()
        # self.label_position.kill()
        # self.label_agent_title.kill()
        # self.label_movements.kill()
        # self.label_total_cost.kill()


