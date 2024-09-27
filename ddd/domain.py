class Agente:
    """Entidad que representa a un agente con su posición y costo acumulado."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.costo_total = 0
