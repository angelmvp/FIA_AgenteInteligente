import tkinter as tk

class SistemaRenderizado:
    """Adaptador de salida que maneja la visualización del mapa y del agente."""
    def __init__(self, root, filas, columnas, cell_size=40):
        self.canvas = tk.Canvas(root, width=columnas * cell_size, height=filas * cell_size)
        self.canvas.pack()
        self.cell_size = cell_size

    def mostrar_mapa(self, mapa):
        for i in range(len(mapa.__grid)):
            for j in range(len(mapa.__grid[0])):
                terreno = mapa.obtener_terreno(i, j)
                color = self.obtener_color(terreno.tipo)
                self.canvas.create_rectangle(j * self.cell_size, i * self.cell_size,
                                             (j + 1) * self.cell_size, (i + 1) * self.cell_size, fill=color)

    def obtener_color(self, tipo):
        if tipo == "Montaña":
            return "gray"
        elif tipo == "Tierra":
            return "green"
        elif tipo == "Agua":
            return "blue"
        elif tipo == "Arena":
            return "yellow"
        return "white"

    def actualizar_posicion(self, agente):
        x = agente.__x * self.cell_size
        y = agente.__y * self.cell_size
        self.canvas.create_oval(y, x, y + self.cell_size, x + self.cell_size, fill="red")