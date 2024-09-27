class ControladorAgente:
    """Interfaz del controlador del agente, que define las operaciones que puede realizar."""
    def mover(self, agente, direccion):
        raise NotImplementedError

    def obtener_costo(self, agente):
        raise NotImplementedError

class MoverAgenteCasoDeUso(ControladorAgente):
    """Caso de uso para mover al agente en el mapa."""

    def __init__(self, mapa):
        self.mapa = mapa

    def mover(self, agente, direccion):
        nueva_x, nueva_y = agente.x, agente.y

        if direccion == "arriba":
            nueva_x = max(0, agente.x - 1)
        elif direccion == "abajo":
            nueva_x = min(len(self.mapa.grid) - 1, agente.x + 1)
        elif direccion == "izquierda":
            nueva_y = max(0, agente.y - 1)
        elif direccion == "derecha":
            nueva_y = min(len(self.mapa.grid[0]) - 1, agente.y + 1)

        # Verificamos si la nueva posición es transitable
        terreno = self.mapa.obtener_terreno(nueva_x, nueva_y)
        if terreno.tipo != "Montaña":
            agente.x, agente.y = nueva_x, nueva_y
            agente.costo_total += terreno.costo
            return True
        else:
            return False

    def obtener_costo(self, agente):
        return agente.costo_total

class ControladorTeclado:
    """Adaptador de entrada que captura las teclas y mueve al agente."""
    def __init__(self, caso_de_uso, agente, render):
        self.caso_de_uso = caso_de_uso
        self.agente = agente
        self.render = render

    def manejar_entrada(self, event):
        direccion = None
        if event.keysym == "Up":
            direccion = "arriba"
        elif event.keysym == "Down":
            direccion = "abajo"
        elif event.keysym == "Left":
            direccion = "izquierda"
        elif event.keysym == "Right":
            direccion = "derecha"

        if direccion:
            exito = self.caso_de_uso.mover(self.agente, direccion)
            if exito:
                print(f"Agente movido a ({self.agente.x}, {self.agente.y}), costo acumulado: {self.agente.costo_total}")
            else:
                print(f"No se puede mover, obstáculo encontrado.")
            self.render.actualizar_posicion(self.agente)