from abc import abstractmethod

from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment


class Sensor:
    def __init__(self, radius: int):
        self.radius = radius

    @abstractmethod
    def detect(self, agent: Agent, environment: Environment):
        """
        Detecta el entorno y actualiza el conocimiento del agente.
        Este método debe ser implementado por las subclases de cada sensor específico.
        """
        raise NotImplementedError("Este método debe ser implementado en una subclase.")


class TerrainSensor(Sensor):
    def detect(self, agent: Agent, environment: Environment):
        """
        Detecta el tipo de terreno en las celdas cercanas al agente, actualizando su conocimiento
        individual y el mapa global del entorno.
        """
        current_position = agent.position
        for direction in ['up', 'down', 'left', 'right']:
            adjacent_position = environment.get_adjacent_cell(current_position, direction)
            terrain_type = environment.get_cell(adjacent_position)

            # Actualiza el conocimiento individual del agente
            agent.known_map[adjacent_position] = terrain_type

            # Actualiza el conocimiento global del entorno
            environment.update_discovered_map(adjacent_position, terrain_type)