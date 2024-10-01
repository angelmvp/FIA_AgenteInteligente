import pygame as pg
import sys
import os
from agente.seleccionarAgente import SeleccionarAgente
from Sensores.Sensores import SeleccionarSensor
from Mapa.Mapa import MapGame
pg.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MENU_WIDTH = 400  
MAP_WIDTH = SCREEN_WIDTH - MENU_WIDTH #maximo mapa 800 pixeles pero se podari ajuestar automaticametne no se
SIZE_CELDA = 30 #se puede cambiar y cambia el tamaño de todo el mapa namas, se podria ajustar si el tamaño es muy grande
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 0, 0)
GRAY=(128,128,128)
CYAN=(0,255,255)


screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Menu Principal del Juwego")

class MainMenu:
    def __init__(self, game):
        self.options = ["Cargar Mapa", "Seleccionar Agente", "Salir"]
        self.selected_option = 0
        self.title_font = pg.font.SysFont("comicsans", 70)
        self.font = pg.font.SysFont("comicsans", 50)
        self.game = game

    def draw(self):
        screen.fill(BLACK)
        title = self.title_font.render("Menu Principal del Juwego", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            if i == self.selected_option:
                label = self.font.render(option, True, HIGHLIGHT_COLOR)
            else:
                label = self.font.render(option, True, WHITE)
            screen.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, 250 + i * 60))

    def move_cursor(self, direction):
        if direction == "up":
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif direction == "down":
            self.selected_option = (self.selected_option + 1) % len(self.options)

    def select_option(self):
        if self.selected_option == 0:
            self.game.show_map_selection()
        elif self.selected_option == 1:
            self.game.current_view = SeleccionarAgente(self.game.window_surface, self.game.manager)
            print("Sekeccioad")
        elif self.selected_option == 2:
            pg.quit()
            sys.exit()
class LoadMap:
    def __init__(self):
        self.map_data = None
        self.maps_dir = 'resources/map'
        self.maps_list = self.get_maps_list()
        self.selected_map_index = 0

    def get_maps_list(self):
        return [f for f in os.listdir(self.maps_dir) if os.path.isfile(os.path.join(self.maps_dir, f))]

    def load_selected_map(self):
        if self.maps_list:
            selected_map = self.maps_list[self.selected_map_index]
            archivo = os.path.join(self.maps_dir, selected_map)
            self.map_data = self.convert_file(archivo)
            print(self.map_data)

    def convert_file(self, archivo):
        matriz = []
        extension = os.path.splitext(archivo)[1]
        delimitador = ',' if extension == '.csv' else ' '
        with open(archivo, newline='') as archivo:
            for linea in archivo:
                fila = [int(valor) for valor in linea.split(delimitador)]
                matriz.append(fila)
        return matriz

    def get_map(self):
        return self.map_data

class RunMenu:
    def __init__(self, window_surface, manager):
        self.window_surface = window_surface
        self.manager = manager
        self.main_menu = MainMenu(self)
        self.load_map = LoadMap()  # Cambiado para crear una instancia de LoadMap
        self.map_data = None
        self.casilla_selected = None
        self.state = "menu"  # Estado inicial es el menú principal
        self.clock = pg.time.Clock()  # Asegúrate de usar clock en RunMenu
        self.current_view = None  
        self.agent=None
        self.sensor=None
    def show_map_selection(self):
        self.state = "map_selection"

    def draw_map_selection(self):
        screen.fill(BLACK)
        title_font = pg.font.SysFont("comicsans", 70)
        font = pg.font.SysFont("comicsans", 50)
        title = title_font.render("Selecciona un Mapa", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        for i, map_name in enumerate(self.load_map.maps_list):  # Ahora accede correctamente a maps_list
            if i == self.load_map.selected_map_index:
                label = font.render(map_name, True, HIGHLIGHT_COLOR)
            else:
                label = font.render(map_name, True, WHITE)
            screen.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, 250 + i * 60))

    def load_map_data(self):  
        self.load_map.load_selected_map()
        self.map_data = self.load_map.get_map()

    def run(self):
        running = True
        while running:
            time_delta = self.clock.tick(60) / 10000.0  # 60 FPS
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if self.state == "menu":
                        if event.key == pg.K_UP:
                            self.main_menu.move_cursor("up")
                        elif event.key == pg.K_DOWN:
                            self.main_menu.move_cursor("down")
                        elif event.key == pg.K_RETURN:
                            self.main_menu.select_option()
                    elif self.state == "map_selection":
                        if event.key == pg.K_UP:
                            self.load_map.selected_map_index = (self.load_map.selected_map_index - 1) % len(
                                self.load_map.maps_list)
                        elif event.key == pg.K_DOWN:
                            self.load_map.selected_map_index = (self.load_map.selected_map_index + 1) % len(
                                self.load_map.maps_list)
                        elif event.key == pg.K_RETURN:
                            self.load_map.load_selected_map()
                            self.map_data = self.load_map.get_map()
                            self.state = "agent_selection"
                            self.current_view = SeleccionarAgente(self.window_surface, self.manager)

                # También procesamos eventos de pygame_gui
                if self.state=="agent_selection" :
                    self.current_view.process_events(event)
                    self.agent=self.current_view.get_agent()
                    if self.agent is not None:
                        self.state="map_game"
                        self.current_view=None
                        self.current_view=MapGame(self.window_surface,self.manager,self.map_data)
                if self.state=="sensors":
                    self.current_view.process_events(event)
                    self.sensor=self.current_view.get_sensor()
                    if self.sensor is not None:
                        self.state="map_game"
                        self.current_view=None
                        self.current_view=MapGame(self.window_surface,self.manager,self.map_data)
                if self.state=="map_game":
                    self.current_view.process_events(event)
                    self.action_map=self.current_view.get_action()
                    if self.action_map is not None:
                        self.state=self.action_map
                        if self.state=="agent_selection":
                            self.current_view=None
                            self.current_view=SeleccionarAgente(self.window_surface,self.manager)
                        elif self.state=="sensors":
                            self.current_view=None
                            self.current_view=SeleccionarSensor(self.window_surface,self.manager)
                pg.display.flip()
            if self.current_view:
                self.current_view.update(time_delta)

            # Lógica de dibujo dependiendo del estado
            if self.state == "menu":
                self.main_menu.draw()
            elif self.state == "map_selection":
                self.draw_map_selection()
            elif self.state == "agent_selection":
                self.current_view.draw()
                self.current_view.process_events(event) 
                self.manager.process_events(event)
            elif self.state=="game_running":
                self.current_view.draw()
                self.current_view.process_events(event) 
                self.manager.process_events(event)
            elif self.state=="sensors":
                self.current_view.draw()
                self.current_view.process_events(event) 
                self.manager.process_events(event)
            elif self.state=="map_game":
                self.current_view.draw()
                self.current_view.process_events(event) 
                self.manager.process_events(event)
        pg.quit()
        sys.exit()
