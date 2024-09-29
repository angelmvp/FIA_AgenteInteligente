from src.agent.domain.action import Action
from src.environment.domain.environment import Environment
from src.agent.domain.sensor import Sensor
from src.position.domain.position import Position
from enum import Enum


class Agent:
    def __init__(self, name: str, position: Position, environment: Environment):
        self.name = name
        self.position = position
        self.environment = environment
        self.known_map = {}
        self.actions = []
        self.sensors = []

    def add_sensor(self, sensor: Sensor):
        """
        Agrega un sensor al agente.
        """
        self.sensors.append(sensor)

    def add_action(self, action: Action):
        """
        Agrega una acción al agente.
        """
        self.actions.append(action)

    def sense(self):
        """
        Usa los sensores para detectar el entorno y actualizar tanto su propio conocimiento
        como el mapa global descubierto.
        """
        for sensor in self.sensors:
            sensor.detect(self, self.environment)

    def update_position(self, new_position: Position):
        """
        Actualiza la posición del agente y su conocimiento individual, luego sincroniza con el entorno.
        """
        self.position = new_position
        self.sense()

    def remember(self, position: Position):
        """
        Verifica si el agente ha explorado previamente una posición específica.
        """
        return self.known_map.get(position, None)

    def make_decision(self):
        """
        Utiliza su conocimiento individual para tomar decisiones (por ejemplo, qué dirección moverse).
        """
        # Un ejemplo simple de cómo podría tomar decisiones basado en su propio conocimiento
        possible_moves = self.get_possible_moves()
        for move in possible_moves:
            if self.remember(move) is None:  # Si el agente no ha explorado esta celda antes
                return move
        return None  # Si no encuentra una celda nueva, puede implementar otras estrategias (como retroceder)

    def get_possible_moves(self):
        """
        Obtiene las posiciones adyacentes a las que el agente puede moverse.
        """
        possible_moves: list[Position] = []
        for direction in ['up', 'down', 'left', 'right']:
            adjacent_position = self.environment.get_adjacent_cell(self.position, direction)
            possible_moves.append(adjacent_position)
        return possible_moves

    def receive_update(self, updated_info):
        """
        Recibe actualizaciones del entorno si este cambia (ej. un terreno cambia o hay un nuevo obstáculo).
        """
        self.known_map.update(updated_info)  # Actualiza su conocimiento si es necesario


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'
