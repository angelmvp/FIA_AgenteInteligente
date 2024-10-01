import pygame
import pygame_gui
import sys

# Inicializar Pygame
pygame.init()

# Configurar la pantalla en modo pantalla completa
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Mi Videojuego")

# Inicializar pygame_gui
manager = pygame_gui.UIManager(screen.get_size())

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Crear botones del menú principal
button_play = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 - 100), (200, 50)),
                                           text='Jugar',
                                           manager=manager)
button_create = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2), (200, 50)),
                                             text='Crear',
                                             manager=manager)
button_edit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 + 100), (200, 50)),
                                           text='Editar',
                                           manager=manager)
button_exit = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 + 200), (200, 50)),
                                           text='Salir',
                                           manager=manager)

# Lista de mapas
maps = ["Mapa 1", "Mapa 2", "Mapa 3", "Mapa 4", "Mapa 5", "Mapa 6", "Mapa 7", "Mapa 8"]

# Crear lista desplegable para selección de mapa
dropdown_map = pygame_gui.elements.UIDropDownMenu(options_list=maps,
                                                  starting_option=maps[0],
                                                  relative_rect=pygame.Rect((screen.get_width() // 2 - 100, screen.get_height() // 2 - 50), (200, 50)),
                                                  manager=manager)
dropdown_map.hide()

# Estado de la vista actual
view = "menu"

# Bucle principal del juego
clock = pygame.time.Clock()
running = True
while running:
  time_delta = clock.tick(60) / 1000.0
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.USEREVENT:
      if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
        if event.ui_element == button_play:
          view = "select_map"
          button_play.hide()
          button_create.hide()
          button_edit.hide()
          button_exit.hide()
          dropdown_map.show()
        elif event.ui_element == button_create:
          print("Crear")
        elif event.ui_element == button_edit:
          print("Editar")
        elif event.ui_element == button_exit:
          running = False
      elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
        if event.ui_element == dropdown_map:
          print(f"Mapa seleccionado: {event.text}")

    manager.process_events(event)

  # Dibujar la vista actual
  screen.fill(WHITE)
  manager.update(time_delta)
  manager.draw_ui(screen)

  # Actualizar pantalla
  pygame.display.flip()

# Salir del juego
pygame.quit()
sys.exit()
