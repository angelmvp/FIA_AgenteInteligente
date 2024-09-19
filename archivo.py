import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os

SIZE_CELDA = 20 
CASILLAS = {
    "pared": {"color": "red", "costos": {"humano": None, "mono": None, "pulpo": None, "sasquatch": None}},
    "camino": {"color": "white", "costos": {"humano": 1, "mono": 1, "pulpo": 1, "sasquatch": 1}},
    "cerro": {"color": "black", "costos": {"humano": None, "mono": None, "pulpo": None, "sasquatch": 15}},
    "tierra": {"color": "brown", "costos": {"humano": 1, "mono": 2, "pulpo": 2, "sasquatch": 4}},
    "agua": {"color": "blue", "costos": {"humano": 2, "mono": 4, "pulpo": 1, "sasquatch": None}},
    "arena": {"color": "yellow", "costos": {"humano": 3, "mono": 3, "pulpo": None, "sasquatch": 3}},
    "bosque": {"color": "green", "costos": {"humano": 4, "mono": 1, "pulpo": 3, "sasquatch": 4}},
    "pantano": {"color": "purple", "costos": {"humano": 5, "mono": 5, "pulpo": 2, "sasquatch": 5}},
    "nieve": {"color": "magenta", "costos": {"humano": 5, "mono": None, "pulpo": None, "sasquatch": 3}},
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
                self.x=x
                self.y=y
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
        casilla = self.mapa.casillas[self.posicion[1]][self.posicion[0]]
        costo = casilla.obtenerCosto(self.tipo)
        if costo is None:
            return False
        casilla.visitada
        return True
    
    def dibujar(self, canvas):
        x, y = self.posicion
        canvas.create_rectangle(x * SIZE_CELDA, y * SIZE_CELDA,
                                (x + 1) * SIZE_CELDA, (y + 1) * SIZE_CELDA,
                                fill="red", outline="gray")    

def seleccionarArchivo():
    archivo = filedialog.askopenfilename(title="Selecciona archivo")
    if archivo:
        matriz = leerMatriz(archivo)
        repaint(matriz)  
        return matriz
        
def leerMatriz(archivo):
    matriz = []
    extension = os.path.splitext(archivo)[1]  
    if extension == '.csv':
        delimitador = ','  
    else:
        delimitador = ' '  
    with open(archivo, newline='') as archivo:
        for linea in archivo:
            fila= []
            valores=linea.split(delimitador)
            for valor in valores:
                numero=int(valor)
                fila.append(numero)
            matriz.append(fila)
    return matriz

def obtenerTipoCasilla(numero):
    if numero==0:
        return "pared"
    elif numero==1:
        return "camino"
    elif numero==2:
        return "cerro"
    elif numero==3:
        return "tierra"
    elif numero==4:
        return "agua"
    elif numero==5:
        return "arena"
    elif numero==6:
        return "bosque"
    elif numero==7:
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
def mostrarTipoCasilla(event):
    pass
def actualizarTipoCasilla():
    pass
def seleccionarAgente():
    #humano,chango,pulpo,piegrande
    pass
def Run():
    pass




ventana = tk.Tk()
ventana.title("Matriz con Agente")


canvas = tk.Canvas(ventana, width=500, height=500)
canvas.pack()
agente_posicion = [5, 0]
matriz=seleccionarArchivo
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

boton_iniciar= Button(ventana,text="iniciar",command=Run)
boton_iniciar.pack()

ventana.mainloop()
