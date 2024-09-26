import pygame as pg
import sys
import os
from tkinter import filedialog

pg.init()
SCREEN_WIDTH = 1200  
SCREEN_HEIGHT = 600
MENU_WIDTH = 400  
MAP_WIDTH = SCREEN_WIDTH - MENU_WIDTH #maximo mapa 800 pixeles pero se podari ajuestar automaticametne no se
SIZE_CELDA = 30 #se puede cambiar y cambia el tamaño de todo el mapa namas, se podria ajustar si el tamaño es muy grande
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
HIGHLIGHT_COLOR = (255, 0, 0)
GRAY=(128,128,128)
CYAN=(0,255,255)
CASILLAS = {
    "wall": {"color": (0, 0, 0)},
    "road": {"color": (255, 255, 255)},
    "mountain": {"color": (139, 69, 19)},
    "earth": {"color": (210, 180, 140)},
    "water": {"color": (0, 0, 255)},
    "sand": {"color": (255, 255, 0)},
    "forest": {"color": (34, 139, 34)},
    "swamp": {"color": (47, 79, 79)},
    "snow": {"color": (240, 248, 255)}
}

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Menu Principal del Juwego")

class MainMenu:
    def __init__(self, game):
        self.options = ["Cargar Mapa", "Iniciar Mapa", "Salir"]
        self.selected_option = 0
        self.title_font = pg.font.SysFont("comicsans", 70)
        self.font = pg.font.SysFont("comicsans", 50)
        self.game = game
#dibujar el menuprincipalgod
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
#moverse en el menu
    def move_cursor(self, direction):
        if direction == "up":
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif direction == "down":
            self.selected_option = (self.selected_option + 1) % len(self.options)

    def select_option(self):
        if self.selected_option == 0: # pa cargar el archivo
            self.game.load_map()  
        elif self.selected_option == 1:
            self.game.init_default_map(5)# pasarel el paraemtero del tamaño 
        elif self.selected_option == 2:#pa salir
            pg.quit()
            sys.exit()
#se ocupa tkintergod para cargar el archivo nadamas, 
class LoadMap:
    def __init__(self):
        self.map_data=None
    def load_map(self):
        archivo = filedialog.askopenfilename(title="Selecciona archivo")
        if archivo:
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
class Game:
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.map_data = None
        self.casilla_selected = None
        self.state = "menu"  # Estado inicial

    def load_map(self):
        loadMap = LoadMap()
        loadMap.load_map()
        self.map_data = loadMap.get_map()
        self.casilla_selected=None
        self.state = "map"
    def clear_map(self):
        self.map_data=None
    def init_default_map(self, n):
        pass
        #aqui ps pa generar el mapa aleatorio deun tamaño n
    #pa las imagenes una idea de seleccionar el agente
    def loadImages(self):
        human_img = pg.image.load("img/human.png")
        monkey_img = pg.image.load("img/monkey.png")
        octopus_img = pg.image.load("img/octopus.png")
        sasquatch_img = pg.image.load("img/sasquatch.png")

        human_img = pg.transform.scale(human_img, (150, 150))
        monkey_img = pg.transform.scale(monkey_img, (150, 150))
        octopus_img = pg.transform.scale(octopus_img, (150, 150))
        sasquatch_img = pg.transform.scale(sasquatch_img, (150, 150))
        screen.blit(human_img,(SCREEN_WIDTH-200,SCREEN_HEIGHT-200))
    #quiza esto pueda ser otra case para manejar diferentes mapas??
    def draw_map(self):
        if self.map_data:
            font = pg.font.SysFont("comicsans", 20)  # Para las letras y números
            for y in range(len(self.map_data)):
                for x in range(len(self.map_data[y])):
                    casilla_type = self.get_casilla_type(self.map_data[y][x])
                    color = CASILLAS[casilla_type]["color"]
                    pg.draw.rect(screen, color, ( SIZE_CELDA + x * SIZE_CELDA, SIZE_CELDA + y * SIZE_CELDA, SIZE_CELDA, SIZE_CELDA))
                    pg.draw.rect(screen, BLACK, ( SIZE_CELDA + x * SIZE_CELDA, SIZE_CELDA + y * SIZE_CELDA, SIZE_CELDA, SIZE_CELDA), 1)
            for i in range(len(self.map_data[0])):
                label = font.render(chr(65 + i), True, WHITE)
                screen.blit(label, (SIZE_CELDA +i * SIZE_CELDA + SIZE_CELDA // 2 - label.get_width() // 2, 0))

            for i in range(len(self.map_data)):
                label = font.render(str(i + 1), True, WHITE)
                screen.blit(label, (0, SIZE_CELDA + (i * SIZE_CELDA + SIZE_CELDA // 2 - label.get_height() // 2 )))
    #pa pintar la casilla
    def get_casilla_type(self, numero):
        if numero == 0:
            return "wall"
        elif numero == 1:
            return "road"
        elif numero == 2:
            return "mountain"
        elif numero == 3:
            return "earth"
        elif numero == 4:
            return "water"
        elif numero == 5:
            return "sand"
        elif numero == 6:
            return "forest"
        elif numero == 7:
            return "swamp"
        else:
            return "snow"
    #ahorita para mostrar tipo de casilla nadamas, igual puede servir para cambiar el tipo
    def handle_click(self, x, y):
        col = (x-SIZE_CELDA) // SIZE_CELDA
        row = (y-SIZE_CELDA) // SIZE_CELDA
        if col < len(self.map_data[0]) and row < len(self.map_data):
            self.casilla_selected = (row, col)
    #el menu lateral para mostrar el tipo y poder cambiar el valor 
    def draw_menu_casillas(self):
        pg.draw.rect(screen, GRAY, (MAP_WIDTH, 0, MENU_WIDTH, SCREEN_HEIGHT)) 
        font = pg.font.SysFont("comicsans", 20)
        labelAdvance = font.render("Presione Enter para Avanzar a agente",True,WHITE)
        screen.blit(labelAdvance,(SCREEN_WIDTH-MENU_WIDTH,20))
        labelGoBack=font.render("Presione Bakspace parae regresar",True,WHITE)
        screen.blit(labelGoBack,(SCREEN_WIDTH-MENU_WIDTH+50,50))
        if self.casilla_selected:
            row, col = self.casilla_selected
            casilla_type = self.get_casilla_type(self.map_data[row][col])
            label = font.render(f"Selected: {casilla_type}", True, CYAN)
            screen.blit(label, (MAP_WIDTH + 10, 80))
            #change_celda_type?? aqui cambiarle 
    def draw_menu_agent(self):
        pg.draw.rect(screen,WHITE,(MAP_WIDTH,0,MENU_WIDTH,SCREEN_HEIGHT))
        font = pg.font.SysFont("comicsans", 20)
        label=font.render("Aqui va el menu para seleccionar agente, inicio y final del juego",True,BLACK)
        screen.blit(label,(MAP_WIDTH+10,50))
        label2=font.render("Presione backspace para regresar ",True,BLACK)
        screen.blit(label2,(MAP_WIDTH+10,90))
    def draw_game_running(self):
        pg.draw.rect(screen,CYAN,(MAP_WIDTH,0,MENU_WIDTH,SCREEN_HEIGHT))
        font = pg.font.SysFont("comicsans", 20)
        label=font.render("Aqui Se supone ya entroe el juego en accion ",True,BLACK)
        screen.blit(label,(MAP_WIDTH+10,50))
        label2=font.render("Presione r para cargar el agente y reinicar el juego",True,BLACK)
        screen.blit(label2,(MAP_WIDTH+10,90))
        label3=font.render("Presione ESC para REgresar al menu",True,BLACK)
        screen.blit(label3,(MAP_WIDTH+10,120))
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
                    elif self.state == "map":
                        if event.key == pg.K_BACKSPACE:
                            self.state = "menu"
                            self.clear_map()
                        elif event.key == pg.K_RETURN:  
                            print("Escape")
                            self.state = "map_agent"
                    elif self.state == "map_agent":
                        if event.key == pg.K_BACKSPACE:
                            self.state = "map"
                        elif event.key==pg.K_RETURN:
                            self.state="running_game"
                    elif self.state=="running_game":
                        if event.key==pg.K_r:
                            self.state="map_agent"
                        elif event.key==pg.K_ESCAPE:
                            self.state="menu"
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.state == "map":
                        mouse_x, mouse_y = pg.mouse.get_pos()
                        if mouse_x < MAP_WIDTH: 
                            self.handle_click(mouse_x, mouse_y)
            
            if self.state == "menu":
                self.clear_map()
                self.main_menu.draw()
            elif self.state == "map":
                screen.fill(BLACK)  
                self.draw_map()
                self.draw_menu_casillas()
            elif self.state == "map_agent":
                screen.fill(BLACK)
                self.draw_map()  
                self.draw_menu_agent()
                self.loadImages()
            elif self.state=="running_game":
                screen.fill(BLACK)
                self.draw_map()#Aqui se supondria ya debemos de enmascarara de una vez el mapa
                                #pero supongo habra que hacer otro mapa nuevo on ose 
                self.draw_game_running()

            pg.display.flip()

        pg.quit()
        sys.exit()

game = Game()
game.run()