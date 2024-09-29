from src.agent.domain.agent import Agent, Direction


class Action:
    def __init__(self, name: Direction):
        self.name = name  # Nombre de la acción

    def execute(self, agent: Agent):
        """
        Ejecuta la acción sobre el agente. Las subclases deben implementar este método.
        """
        raise NotImplementedError("Este método debe ser implementado en una subclase.")


class MoveAction(Action):
    def __init__(self, direction: Direction):
        super().__init__(direction)
        self.direction = direction  # Dirección de movimiento ('up', 'down', 'left', 'right')

    def execute(self, agent: Agent):
        """
        Mueve al agente en la dirección especificada, actualizando su posición.
        """
        environment = agent.environment
        current_position = agent.position
        new_position = environment.get_adjacent_cell(current_position, self.direction)

        # Actualizar la posición del agente
        agent.update_position(new_position)