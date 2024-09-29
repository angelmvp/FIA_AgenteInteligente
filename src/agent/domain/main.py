# Inicializar el entorno
from src.agent.domain.agent import Agent
from src.environment.domain.environment import Environment
from src.agent.domain.sensor import TerrainSensor
from src.map.domain.map import Cell
from src.environment.domain.terrain.terrain import TerrainRepository
from src.position.domain.position import Position


def display_discovered_map(environment: Environment):
    """
    Muestra el mapa global descubierto hasta el momento.
    """
    discovered_map = environment.get_discovered_map()
    for row in discovered_map:
        print(" ".join([str(cell) if cell is not None else "?" for cell in row]))


terrain_repository = TerrainRepository('../../../resources/terrain/terrain.json')
mountain_terrain = terrain_repository.get(0)

environment_grid = [[Cell(0, 0, mountain_terrain), 1, 0], [1, 1, 1], [0, 1, 0]]  # Mapa de ejemplo
environment = Environment(environment_grid)

# Crear agentes
agent1 = Agent("Agente 1", Position(0, 0), environment)

# Añadir sensores al agente
sensor = TerrainSensor(1)
agent1.sensors.append(sensor)

# Añadir agentes al entorno
environment.add_agent(agent1)

# El agente detecta su entorno y actualiza su conocimiento individual y el global
agent1.sense()

# Mostrar el mapa global descubierto
display_discovered_map(environment)

# El agente toma una decisión basada en su conocimiento y se mueve
new_position = agent1.make_decision()
if new_position:
    environment.move_agent(agent1, new_position)

# Mostrar el mapa global después del movimiento
display_discovered_map(environment)

# El agente revisa su propio conocimiento local
print(agent1.known_map)
