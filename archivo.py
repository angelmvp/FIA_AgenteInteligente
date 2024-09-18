import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

SIZE_CELDA = 20 
CASILLAS = {
    "cerro": {"color": "black", "costos": {"humano": None, "mono": None, "pulpo": None, "sasquatch": 15}},
    "tierra": {"color": "brown", "costos": {"humano": 1, "mono": 2, "pulpo": 2, "sasquatch": 4}},
    "agua": {"color": "blue", "costos": {"humano": 2, "mono": 4, "pulpo": 1, "sasquatch": None}},
    "arena": {"color": "yellow", "costos": {"humano": 3, "mono": 3, "pulpo": None, "sasquatch": 3}},
    "bosque": {"color": "green", "costos": {"humano": 4, "mono": 1, "pulpo": 3, "sasquatch": 4}},
    "pantano": {"color": "purple", "costos": {"humano": 5, "mono": 5, "pulpo": 2, "sasquatch": 5}},
    "nieve": {"color": "gray", "costos": {"humano": 5, "mono": None, "pulpo": None, "sasquatch": 3}},
}
class Casilla:
    def __init__(self,tipo):
        self.tipo=tipo
        self.color=CASILLAS[tipo]["color"]
        self.visitada=False
        self.costo=CASILLAS[tipo]["costos"]
    def dibujar(self,canvas,x,y):
                canvas.create_rectangle(x * SIZE_CELDA, y * SIZE_CELDA,
                                (x + 1) * SIZE_CELDA, (y + 1) * SIZE_CELDA,
                                fill=self.color, outline="gray")
    def visitada(self):
        self.visitada=True
    def obtenerCosto(self,objeto):
        costo=self.costo.get(objeto,None)

class Agente:
    def __init__(self,tipo,posicion,mapa):
        self.tipo=tipo
        self.posicion=posicion
        self.mapa=mapa
    def mover(self, direccion):
        x, y = self.posicion
        if direccion == 'Left' and x > 0:
            self.posicion[0] -= 1
        elif direccion == 'Right' and x < len(self.mapa.casillas[0]) - 1:
            self.posicion[0] += 1
        elif direccion == 'Up' and y > 0:
            self.posicion[1] -= 1
        elif direccion == 'Down' and y < len(self.mapa.casillas) - 1:
            self.posicion[1] += 1
        casilla = self.mapa.casillas[self.posicion[1]][self.posicion[0]]
        costo = casilla.obtenerCosto(self.tipo)
        if costo is None:
            return False
        casilla.visitada
        print(f"El {self.tipo_ser} se movió a {self.posicion} con un costo de {costo}.")
        return True
    
    def dibujar(self, canvas):
        x, y = self.posicion
        canvas.create_rectangle(x * SIZE_CELDA, y * SIZE_CELDA,
                                (x + 1) * SIZE_CELDA, (y + 1) * SIZE_CELDA,
                                fill="red", outline="gray")    




def leerMatriz(archivo):
    matriz = []
    extension = os.path.splitext(archivo)[1]  
    if extension == '.csv':
        delimitador = ','  
    else:
        delimitador = ' '  
    with open(archivo, newline='') as archivo:
        for linea in archivo:
            fila_convertida = [int(valor) for valor in linea.strip().split(delimitador)]
            matriz.append(fila_convertida)
    return matriz

def seleccionarArchivo():
    archivo = filedialog.askopenfilename(title="Selecciona archivo")
    if archivo:
        matriz = leerMatriz(archivo)
        repaint(matriz)  
        return matriz
def obtenerTipoCasilla(numero):
    if numero==1:
        return "cerro"
    elif numero==2:
        return "tierra"
    elif numero==3:
        return "agua"
    elif numero==4:
        return "arena"
    elif numero==5:
        return "bosque"
    elif numero==6:
        return "pantano"
    else:
        return "nieve" 
def dibujarMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            tipo_casilla = obtenerTipoCasilla(matriz[i][j])  
            casilla = Casilla(tipo_casilla)
            casilla.dibujar(canvas, j, i)
def repaint(nueva_matriz):
    global matriz
    matriz = nueva_matriz
    canvas.config(width=len(matriz[0]) * SIZE_CELDA, height=len(matriz) * SIZE_CELDA)
    dibujarMatriz(matriz)
    agente.dibujar(canvas)

def mover_agente(event):
    direccion = event.keysym  
    if not agente.mover(direccion): 
        print("Movimiento no permitido.")
        return
    canvas.delete("all")  
    dibujarMatriz(matriz) 




ventana = tk.Tk()
ventana.title("Matriz con Agente")


canvas = tk.Canvas(ventana, width=500, height=500)
canvas.pack()
agente_posicion = [5, 0]
matriz=seleccionarArchivo()
agente=Agente(tipo="humano",posicion=agente_posicion,mapa=matriz)
agente.dibujar(canvas)




menu_principal= Menu(ventana)
ventana.config(menu=menu_principal)
menu_archivo=Menu(menu_principal,tearoff=0)
menu_juego=Menu(menu_principal)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_principal.add_cascade(label="Modificar Mapa",menu=menu_juego)
menu_archivo.add_command(label="Cargar Nuevo Archivo", command=seleccionarArchivo)
#menu_archivo.add_command(label="Guardar Mapa",command=guardarMapa)
#menu_archivo.add_command(label="Generar Aleatorio",command=mapaAleatorio)

boton_iniciar= Button(ventana,text="iniciar",command=dibujarMatriz)
boton_iniciar.pack()
ventana.mainloop()
