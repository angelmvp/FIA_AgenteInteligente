import pygame as pg
import random
import queue

# Definir dimensiones del mapa
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
MENU_WIDTH = 400  
MAP_WIDTH = SCREEN_WIDTH - MENU_WIDTH
SIZE_CELDA = 30

# Colores de los tipos de terreno
COLOR_MONTAÑA = (128, 128, 128)  # Gris
COLOR_TIERRA = (250, 191, 143)   # Beige claro
COLOR_AGUA = (2, 175, 255)       # Azul claro
COLOR_ARENA = (255, 191, 0)      # Amarillo
COLOR_BOSQUE = (150, 210, 80)    # Verde

# Inicializar pygame
pg.init()
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Mapa Aleatorio con Expansión por Regiones")

# Función para inicializar el mapa con un valor neutral (-1)
def inicializar_mapa(filas, columnas):
    return [[-1 for _ in range(columnas)] for _ in range(filas)]

# Función para expandir un terreno desde un punto inicial
def expandir_terreno(mapa, tipo_terreno, inicio_fila, inicio_columna, tamano_region):
    filas = len(mapa)
    columnas = len(mapa[0])
    visitados = set()
    q = queue.Queue()
    q.put((inicio_fila, inicio_columna))
    visitados.add((inicio_fila, inicio_columna))
    mapa[inicio_fila][inicio_columna] = tipo_terreno
    contador = 1

    # Desplazamientos para las 4 direcciones (arriba, abajo, izquierda, derecha)
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while not q.empty() and contador < tamano_region:
        fila, columna = q.get()

        # Expandir en las 4 direcciones
        for dir_fila, dir_columna in direcciones:
            nueva_fila = fila + dir_fila
            nueva_columna = columna + dir_columna

            # Verificar si está dentro de los límites y no ha sido visitado
            if (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas and
                (nueva_fila, nueva_columna) not in visitados and mapa[nueva_fila][nueva_columna] == -1):
                mapa[nueva_fila][nueva_columna] = tipo_terreno
                visitados.add((nueva_fila, nueva_columna))
                q.put((nueva_fila, nueva_columna))
                contador += 1
                if contador >= tamano_region:
                    break

# Función para generar un mapa aleatorio con expansión por regiones
def generar_mapa(filas, columnas):
    mapa = inicializar_mapa(filas, columnas)
    
    # Definir tamaños de regiones y puntos de inicio para cada tipo de terreno
    regiones = {
        'agua': {'tipo': 2, 'tamaño': random.randint(30, 60), 'centros': 3},
        'arena': {'tipo': 3, 'tamaño': random.randint(20, 50), 'centros': 2},
        'bosque': {'tipo': 4, 'tamaño': random.randint(50, 80), 'centros': 3},
        'tierra': {'tipo': 1, 'tamaño': random.randint(70, 100), 'centros': 4},
        'montaña': {'tipo': 0, 'tamaño': random.randint(40, 70), 'centros': 2}
    }
    
    # Expandir cada tipo de terreno desde múltiples puntos iniciales
    for terreno, config in regiones.items():
        for _ in range(config['centros']):
            inicio_fila = random.randint(0, filas - 1)
            inicio_columna = random.randint(0, columnas - 1)
            expandir_terreno(mapa, config['tipo'], inicio_fila, inicio_columna, config['tamaño'])
    
    # Rellenar el resto del mapa con tierra (valor 1)
    for fila in range(filas):
        for columna in range(columnas):
            if mapa[fila][columna] == -1:
                mapa[fila][columna] = 1

    return mapa

# Función para dibujar el mapa con los colores correspondientes a cada tipo de terreno
def dibujar_mapa(mapa):
    for fila in range(len(mapa)):
        for columna in range(len(mapa[fila])):
            celda = mapa[fila][columna]
            if celda == 0:
                color = COLOR_MONTAÑA
            elif celda == 1:
                color = COLOR_TIERRA
            elif celda == 2:
                color = COLOR_AGUA
            elif celda == 3:
                color = COLOR_ARENA
            elif celda == 4:
                color = COLOR_BOSQUE

            # Dibujar cada celda
            pg.draw.rect(screen, color, pg.Rect(columna * SIZE_CELDA, fila * SIZE_CELDA, SIZE_CELDA, SIZE_CELDA))

def main():
    filas = SCREEN_HEIGHT // SIZE_CELDA
    columnas = MAP_WIDTH // SIZE_CELDA
    mapa = generar_mapa(filas, columnas)

    # Loop principal del juego
    corriendo = True
    while corriendo:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                corriendo = False

        screen.fill((0, 0, 0))  # Fondo negro
        dibujar_mapa(mapa)
        pg.display.flip()

    pg.quit()

if __name__ == "__main__":
    main()
