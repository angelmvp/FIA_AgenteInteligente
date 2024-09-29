import tkinter as tk

from domain import Mapa, Agente
from application import MoverAgenteCasoDeUso, ControladorTeclado
from infrastructure import SistemaRenderizado

def main():
    # Crear la ventana de tkinter
    root = tk.Tk()
    root.title("Simulación de Agentes con Arquitectura Hexagonal")

    # Crear el mapa y las entidades
    mapa = Mapa(15, 15)
    mapa.load_map('../map/maze.csv')

    # Crear al agente
    agente = Agente(7, 7)

    # Crear el caso de uso para mover al agente
    caso_de_uso = MoverAgenteCasoDeUso(mapa)

    # Crear el sistema de renderizado
    render = SistemaRenderizado(root, 15, 15)

    # Dibujar el mapa
    render.mostrar_mapa(mapa)
    render.actualizar_posicion(agente)

    # Controlar el agente con el teclado
    controlador_teclado = ControladorTeclado(caso_de_uso, agente, render)

    root.bind("<Key>", controlador_teclado.manejar_entrada)
    root.mainloop()

if __name__ == "__main__":
    main()