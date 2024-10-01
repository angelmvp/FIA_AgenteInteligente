import pygame
import pygame_gui
import sys
import os
from front.menu.menu import RunMenu 

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700

def main():
    pygame.init()
    window_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT), theme_path="styles.json")
    manager.get_theme().load_theme("front/agente/Styles.json")
    manager.get_theme().load_theme('front/agente/buttonAgents.json')
    manager.get_theme().load_theme('front/Sensores/buttonSensores.json')
    manager.get_theme().load_theme('front/Sensores/StylesSensors.json')
    
    menu = RunMenu(window_surface, manager)
    menu.run()  
    pygame.quit()

if __name__ == '__main__':
    main()
