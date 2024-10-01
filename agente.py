# import pygame
# import pygame_gui
# from pygame_gui.core import ObjectID

# SCREEN_WIDTH=1000
# SCREEN_HEIGHT=700
# MENU_WIDTH=300
# TITLE_HEIGHT=100
# IMAGE_WIDTH=MENU_WIDTH//2
# IMAGE_HEIGHT=IMAGE_WIDTH
# PADDING_IMG=10
# BUTTON_WIDTH=150
# BUTTON_HEIGHT=TITLE_HEIGHT//2
# MENU_INSTRUCTIONS_HEIGHT = (SCREEN_HEIGHT-TITLE_HEIGHT)//2

# pygame.init()
# pygame.display.set_caption('Agent Menu')
# window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
# background.fill(pygame.Color('#000000'))

# manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), theme_path="styles.json")
# manager.get_theme().load_theme('buttonStyles.json')
# #manager.get_theme().load_theme('.json')
# clock =pygame.time.Clock()

# # Todo lo del header
# panel_header_rect=pygame.Rect(0,0,SCREEN_WIDTH,TITLE_HEIGHT)
# panel_header=pygame_gui.elements.UIPanel(relative_rect=panel_header_rect,
#                                          manager=manager,
#                                          object_id=ObjectID(class_id='@panel_header'))
# button_back_rect = pygame.Rect(20,TITLE_HEIGHT//4, BUTTON_WIDTH, BUTTON_HEIGHT)
# button_advance_rect=pygame.Rect(SCREEN_WIDTH-BUTTON_WIDTH-20,TITLE_HEIGHT//4,BUTTON_WIDTH,BUTTON_HEIGHT)
# button_back=pygame_gui.elements.UIButton(relative_rect=button_back_rect,
#                                         text="Regresar",
#                                         manager=manager,
#                                         container=panel_header,
#                                         object_id=ObjectID(class_id='@buttons_navegation'))
# button_advance=pygame_gui.elements.UIButton(relative_rect=button_advance_rect,
#                                         text="Avanzar",
#                                         manager=manager,
#                                         container=panel_header,
#                                         object_id=ObjectID(class_id='@buttons_navegation'))

# label_title_rect=pygame.Rect(SCREEN_WIDTH//4,TITLE_HEIGHT//4,SCREEN_WIDTH//2,TITLE_HEIGHT//2)
# label_title_map=pygame_gui.elements.UILabel(relative_rect=label_title_rect,
#                                                 text='INICIALIZACION DE JUEGO',
#                                                 manager=manager,
#                                                 container=panel_header,
#                                             object_id=ObjectID(class_id='@title',
#                                                                object_id='#title_map_modified'))

# rect_instructions = pygame.Rect(
#     SCREEN_WIDTH - MENU_WIDTH, 
#     TITLE_HEIGHT, 
#     MENU_WIDTH, 
#     SCREEN_HEIGHT - MENU_INSTRUCTIONS_HEIGHT-TITLE_HEIGHT
# )


# rect_label_instructions = pygame.Rect(0, 0, MENU_WIDTH - 20, 300)
# rect_label_instructions.top=(-30)
# menu_instructions_agent = pygame_gui.elements.UIPanel(
#     relative_rect=rect_instructions,
#     manager=manager,
#     object_id=ObjectID(class_id='@menu_container_instructions')
# )

# label_instrucciones = pygame_gui.elements.UILabel(
#     relative_rect=rect_label_instructions,
#     text=('Para Seleccionar un Agente, presione en la \n'
#           'imagen del agente. Para seleccionar el\n'
#           'inicio del agente presione una celda con\n'
#           'CLICK IZQUIERDO y para seleccionar la\n'
#           'celda final presione CLICK DERECHO sobre\n'
#           'la celda. \n'
#           'POR FAVOR SELECCIONE UN AGENTE.'),
#     manager=manager,
#     container=menu_instructions_agent,
#     anchors={"top":"top"},
#     object_id=ObjectID(class_id='@instructions')
# )

# menu_container_img = pygame_gui.elements.UIPanel(
#             relative_rect=pygame.Rect(SCREEN_WIDTH-MENU_WIDTH,
#             TITLE_HEIGHT+MENU_INSTRUCTIONS_HEIGHT,
#             MENU_WIDTH,
#             SCREEN_HEIGHT-TITLE_HEIGHT-MENU_INSTRUCTIONS_HEIGHT),
#             manager=manager,
#             object_id=ObjectID(class_id='@menu_container_img'))

# human_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect(PADDING_IMG, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
#     text='',
#     manager=manager,
#     container=menu_container_img,
#     object_id=ObjectID(class_id='@img_button', object_id='#human_button')
# )

# monkey_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect(MENU_WIDTH // 2, PADDING_IMG, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
#     text='',
#     manager=manager,
#     container=menu_container_img,
#     object_id=ObjectID(class_id='@img_button', object_id='#monkey_button')
# )

# octopus_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect(PADDING_IMG, (SCREEN_HEIGHT - TITLE_HEIGHT - MENU_INSTRUCTIONS_HEIGHT) // 2, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
#     text='',
#     manager=manager,
#     container=menu_container_img,
#     object_id=ObjectID(class_id='@img_button', object_id='#octopus_button')
# )

# sasquatch_button = pygame_gui.elements.UIButton(
#     relative_rect=pygame.Rect(MENU_WIDTH // 2, (SCREEN_HEIGHT - TITLE_HEIGHT - MENU_INSTRUCTIONS_HEIGHT) // 2, IMAGE_WIDTH - PADDING_IMG, IMAGE_HEIGHT - PADDING_IMG),
#     text='',
#     manager=manager,
#     container=menu_container_img,
#     object_id=ObjectID(class_id='@img_button', object_id='#sasquatch_button')
# )
# map_rect=pygame.Rect(0,TITLE_HEIGHT,SCREEN_WIDTH-MENU_WIDTH,SCREEN_HEIGHT-TITLE_HEIGHT)
# is_running = True
# while is_running:
#     time_delta=clock.tick(600000)/1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False
#         if event.type == pygame_gui.UI_BUTTON_PRESSED:
#             if event.ui_element == button_advance:
#                 print('avanzar')
#             elif event.ui_element==button_back:
#                 print('retroceder')    
#             elif event.ui_element == human_button:
#                 print('Humano seleccionado')
#             elif event.ui_element == monkey_button:
#                 print('Mono seleccionado')
#             elif event.ui_element == octopus_button:
#                 print('Pulpo seleccionado')
#             elif event.ui_element == sasquatch_button:
#                 print('Sasquatch seleccionado')
#         manager.process_events(event)
#     manager.update(time_delta)
#     window_surface.blit(background, (0, 0))
#     manager.draw_ui(window_surface)
#     pygame.display.update()