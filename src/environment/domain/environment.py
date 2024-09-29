from src.agent.domain.agent import Direction, Agent
from src.environment.domain.cell import Cell
from src.position.domain.position import Position


class Environment:
    def __init__(self, grid: list[list[Cell]]):
        self.grid: list[list[Cell]] = grid
        self.discovered_map: list[list[Cell or None]] = [[None for _ in row] for row in grid]
        self.agents: list[Agent] = []
        self.subscribers: list[Agent] = []

    def add_agent(self, agent: Agent):
        """
        Añadir un agente al entorno.
        """
        self.agents.append(agent)
        self.subscribers.append(agent)

    def get_cell(self, position: Position) -> Cell:
        """
        Devuelve el estado del terreno en una posición específica.
        """
        return self.grid[position.x][position.y]

    def update_discovered_map(self, position: Position, value: Cell or None):
        """
        Actualiza el mapa global descubierto en una posición específica.
        """
        self.discovered_map[position.x][position.y] = value

    def get_discovered_map(self) -> list[list[Cell or None]]:
        """
        Devuelve el mapa global descubierto.
        """
        return self.discovered_map

    def update_state(self, position: Position, new_value: Cell):
        """
        Cambia el estado del entorno en una posición y actualiza tanto el mapa global como el de los agentes.
        """
        self.grid[position.x][position.y] = new_value
        self.update_discovered_map(position, new_value)
        self.notify_agents({position: new_value})

    def notify_agents(self, update_info: dict[Position, Cell]):
        """
        Notifica a los agentes suscritos sobre cambios en el entorno.
        """
        for agent in self.subscribers:
            agent.receive_update(update_info)

    def move_agent(self, agent: Agent, new_position: Position):
        """
        Mueve al agente en el entorno y actualiza el mapa global descubierto según lo que explore.
        """
        terrain_type = self.get_cell(new_position)
        self.update_discovered_map(new_position, terrain_type)
        agent.update_position(new_position)

    def get_adjacent_cell(self, position: Position, direction: Direction) -> Position:
        """
        Obtiene la posición adyacente a una posición y dirección dadas.
        :param position: La posición actual.
        :param direction: La dirección en la que se desea mover.
        :return: La posición adyacente.
        """
        x, y = position.x, position.y
        if direction == 'up':
            return Position(x - 1, y)
        if direction == 'down':
            return Position(x + 1, y)
        if direction == 'left':
            return Position(x, y - 1)
        if direction == 'right':
            return Position(x, y + 1)
        raise ValueError("Dirección inválida.")