import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla en modo pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Mi Videojuego")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (100, 100, 100)

# Cargar la fuente Comic Sans
font_large = pygame.font.SysFont("comicsansms", 96)
font_normal = pygame.font.SysFont("comicsansms", 64)

# Renderizar los textos del menú principal
text_main_menu = font_large.render("Menú Principal", True, BLACK)
text_play = font_normal.render("Jugar", True, BLACK)
text_create = font_normal.render("Crear", True, BLACK)
text_edit = font_normal.render("Editar", True, BLACK)
text_exit = font_normal.render("Salir", True, BLACK)

# Calcular las posiciones para centrar los textos del menú principal
screen_rect = screen.get_rect()
text_main_menu_rect = text_main_menu.get_rect(center=(screen_rect.centerx, screen_rect.centery - 300))
text_play_rect = text_play.get_rect(center=(screen_rect.centerx, screen_rect.centery - 100))
text_create_rect = text_create.get_rect(center=(screen_rect.centerx, screen_rect.centery))
text_edit_rect = text_edit.get_rect(center=(screen_rect.centerx, screen_rect.centery + 100))
text_exit_rect = text_exit.get_rect(center=(screen_rect.centerx, screen_rect.centery + 200))

# Lista de opciones del menú
menu_options = [text_play_rect, text_create_rect, text_edit_rect, text_exit_rect]
selected_option = 0

# Lista de mapas
maps = ["Mapa 1", "Mapa 2", "Mapa 3", "Mapa 4", "Mapa 5", "Mapa 6", "Mapa 7", "Mapa 8"]

# Renderizar los textos de la vista de selección de mapa
text_select_map = font_large.render("Seleccionar Mapa", True, BLACK)

# Calcular las posiciones para centrar los textos de la vista de selección de mapa
text_select_map_rect = text_select_map.get_rect(center=(screen_rect.centerx, screen_rect.centery - 200))

# Estado de la vista actual
view = "menu"
selected_map = 0
scroll_offset = 0


def draw_rounded_rect(surface, color, rect, corner_radius, border_width):
  """ Draw a rectangle with rounded corners and transparent background. """
  # Draw the filled rounded rectangle
  pygame.draw.rect(surface, color, rect, border_radius=corner_radius, width=border_width)


def draw_menu():
  screen.fill(WHITE)
  screen.blit(text_main_menu, text_main_menu_rect)
  for i, rect in enumerate(menu_options):
    if i == selected_option:
      pygame.draw.line(screen, HIGHLIGHT, (rect.left, rect.bottom + 5), (rect.right, rect.bottom + 5), 5)
    screen.blit([text_play, text_create, text_edit, text_exit][i], rect)


def draw_select_map():
  screen.fill(WHITE)
  screen.blit(text_select_map, text_select_map_rect)

  # Definir el área del recuadro de selección de mapa
  map_box_rect = pygame.Rect(screen_rect.centerx - 500, screen_rect.centery - 50, 1000, 400)
  draw_rounded_rect(screen, BLACK, map_box_rect, 20, 3)

  # Dibujar los mapas dentro del recuadro con scroll
  for i, map_name in enumerate(maps):
    map_text = font_normal.render(map_name, True, BLACK)
    map_rect = map_text.get_rect(center=(map_box_rect.centerx, map_box_rect.top + 50 + i * 100 - scroll_offset))
    if map_box_rect.top <= map_rect.top <= map_box_rect.bottom - map_text.get_height():
      if i == selected_map:
        pygame.draw.line(screen, HIGHLIGHT, (map_rect.left, map_rect.bottom + 5), (map_rect.right, map_rect.bottom + 5), 5)
      screen.blit(map_text, map_rect)


# Bucle principal del juego
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.KEYDOWN:
      if view == "menu":
        if event.key == pygame.K_DOWN:
          selected_option = (selected_option + 1) % len(menu_options)
        elif event.key == pygame.K_UP:
          selected_option = (selected_option - 1) % len(menu_options)
        elif event.key == pygame.K_RETURN:
          if selected_option == 0:
            view = "select_map"
          elif selected_option == 1:
            print("Crear")
          elif selected_option == 2:
            print("Editar")
          elif selected_option == 3:
            running = False
      elif view == "select_map":
        if event.key == pygame.K_DOWN:
          if selected_map < len(maps) - 1:
            selected_map += 1
            if selected_map * 100 + 50 - scroll_offset > 300:
              scroll_offset += 100
        elif event.key == pygame.K_UP:
          if selected_map > 0:
            selected_map -= 1
            if selected_map * 100 + 50 - scroll_offset < 0:
              scroll_offset -= 100
        elif event.key == pygame.K_RETURN:
          print(f"Mapa seleccionado: {maps[selected_map]}")
        elif event.key == pygame.K_BACKSPACE:
          view = "menu"

  # Dibujar la vista actual
  if view == "menu":
    draw_menu()
  elif view == "select_map":
    draw_select_map()

  # Actualizar pantalla
  pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()
