import pygame as pg
import sys
import os

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
        self.options = ["Cargar Mapa", "Iniciar Mapa", "Salir"]
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
            Cambiar a una nueva Vista la de agente
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
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.map_data = None
        self.casilla_selected = None
        self.state = "menu"  # Estado inicial
        self.load_map = LoadMap()

    def show_map_selection(self):
        self.state = "map_selection"

    def draw_map_selection(self):
        screen.fill(BLACK)
        title_font = pg.font.SysFont("comicsans", 70)
        font = pg.font.SysFont("comicsans", 50)
        title = title_font.render("Selecciona un Mapa", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 100))

        for i, map_name in enumerate(self.load_map.maps_list):
            if i == self.load_map.selected_map_index:
                label = font.render(map_name, True, HIGHLIGHT_COLOR)
            else:
                label = font.render(map_name, True, WHITE)
            screen.blit(label, (SCREEN_WIDTH // 2 - label.get_width() // 2, 250 + i * 60))

    def load_map(self):
        loadMap = LoadMap()
        loadMap.load_map()
        self.map_data = loadMap.get_map()
        self.casilla_selected=None
        self.state = "map"
    def run(self):
        running = True
        while running:
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
            if self.state == "menu":
                self.clear_map()
                self.main_menu.draw()
            elif self.state == "map_selection":
                self.draw_map_selection()

            pg.display.flip()

        pg.quit()
        sys.exit()

game = RunMenu()
game.run()