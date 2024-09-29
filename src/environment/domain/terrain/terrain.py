class Terrain:
    """Entidad que representa un tipo de terreno en el mapa."""

    def __init__(self, display_name: str, color: str, movement_costs: dict[str, int]):
        self.display_name = display_name
        self.color = color
        self.movement_costs = movement_costs

    def get_movement_cost(self, movement_type: str) -> int or None:
        """
        Retorna el costo de movimiento para un tipo de movimiento.

        Args:
            movement_type (str): Tipo de movimiento.

        Returns:
            int or None: Costo de movimiento.
        """
        return self.movement_costs.get(movement_type)

    def __str__(self):
        return f"Terrain(display_name={self.display_name}, color={self.color}, movement_costs={self.movement_costs})"
