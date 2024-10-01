from src.agent.domain.agent import Agent
from src.environment.domain.terrain.terrain import Terrain
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map import Map
from src.map.domain.map_repository import MapRepository

if __name__ == '__main__':
  terrain_repository: TerrainRepository = TerrainRepository()
  terrain_repository.load_from_file('../resources/terrain/terrain.json')
  mountain_terrain: Terrain = terrain_repository.get_by_code(0)
  print(mountain_terrain)
  print('Costo de movimiento para humano:', mountain_terrain.get_movement_cost('human'))
  print('Costo de movimiento para mono:', mountain_terrain.get_movement_cost('monkey'))
  print('Costo de movimiento para pulpo:', mountain_terrain.get_movement_cost('octopus'))
  print('Costo de movimiento para pie grande:', mountain_terrain.get_movement_cost('sasquatch'))

  map_repository: MapRepository = MapRepository('../resources/map')
  maze_map: Map = map_repository.load('maze.csv')
  maze_map.print()

  known_map = [[None for _ in range(maze_map.get_rows())] for _ in range(maze_map.get_columns())]
  agent1 = Agent(0, [], None, None, known_map, 'agent1', [], 0, 0, 0)
  agent1.set_known(0, 0)
  agent1.get_environment()
