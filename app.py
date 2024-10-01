import os

from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.action.move_down_action import MoveDownAction
from src.agent.domain.action.move_left_action import MoveLeftAction
from src.agent.domain.action.move_right_action import MoveRightAction
from src.agent.domain.action.move_up_action import MoveUpAction
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.down_directional_sensor import DownDirectionalSensor
from src.agent.domain.sensor.left_directional_sensor import LeftDirectionalSensor
from src.agent.domain.sensor.merged_sensor import MergedSensor
from src.agent.domain.sensor.right_directional_sensor import RightDirectionalSensor
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor_repository import SensorRepository
from src.agent.domain.sensor.up_directional_sensor import UpDirectionalSensor
from src.environment.application.environment_agent_service import EnvironmentAgentService, ExecuteActionResult, ResultCode, ExecuteSensorResult
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.environment import Environment
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map import Map
from src.map.domain.map_repository import MapRepository

if __name__ == '__main__':
  project_root = os.path.dirname(os.path.abspath(__file__))

  terrain_repository: TerrainRepository = TerrainRepository(f'{project_root}/resources/terrain')
  terrain_repository.load_from_file('maze.json')

  map_repository: MapRepository = MapRepository(f'{project_root}/resources/map')
  maze_map: Map = map_repository.load('maze.csv')
  maze_map.print()

  environment_service: EnvironmentService = EnvironmentService(terrain_repository)
  environment: Environment = environment_service.create_environment_from_map(maze_map)

  action_repository: ActionRepository = ActionRepository()
  action_repository.add_actions(MoveUpAction(), MoveDownAction(), MoveLeftAction(), MoveRightAction())

  sensor_repository: SensorRepository = SensorRepository()
  up_directional_sensor: UpDirectionalSensor = UpDirectionalSensor()
  down_directional_sensor: DownDirectionalSensor = DownDirectionalSensor()
  left_directional_sensor: LeftDirectionalSensor = LeftDirectionalSensor()
  right_directional_sensor: RightDirectionalSensor = RightDirectionalSensor()
  sensor_repository.add_sensors(
    up_directional_sensor,
    down_directional_sensor,
    left_directional_sensor,
    right_directional_sensor,
    MergedSensor('up_down', [up_directional_sensor, down_directional_sensor]),
    MergedSensor('left_right', [left_directional_sensor, right_directional_sensor]),
    MergedSensor('every_direction', [up_directional_sensor, down_directional_sensor, left_directional_sensor, right_directional_sensor])
  )

  environment_agent_service: EnvironmentAgentService = EnvironmentAgentService(action_repository, sensor_repository)

  known_map = [[None for _ in range(maze_map.get_rows())] for _ in range(maze_map.get_columns())]
  human_agent = Agent(
    0,
    {
      MoveUpAction.IDENTIFIER: ActionConfiguration(MoveUpAction.IDENTIFIER, {'steps': 1}),
      MoveDownAction.IDENTIFIER: ActionConfiguration(MoveDownAction.IDENTIFIER, {'steps': 1}),
      MoveLeftAction.IDENTIFIER: ActionConfiguration(MoveLeftAction.IDENTIFIER, {'steps': 1}),
      MoveRightAction.IDENTIFIER: ActionConfiguration(MoveRightAction.IDENTIFIER, {'steps': 2})
    },
    None,
    known_map,
    'human',
    {
      UpDirectionalSensor.IDENTIFIER: SensorConfiguration(UpDirectionalSensor.IDENTIFIER, False, 1),
      DownDirectionalSensor.IDENTIFIER: SensorConfiguration(DownDirectionalSensor.IDENTIFIER, False, 1),
      LeftDirectionalSensor.IDENTIFIER: SensorConfiguration(LeftDirectionalSensor.IDENTIFIER, False, 1),
      RightDirectionalSensor.IDENTIFIER: SensorConfiguration(RightDirectionalSensor.IDENTIFIER, False, 1),
      'up_down': SensorConfiguration('up_down', False, 1),
      'left_right': SensorConfiguration('left_right', False, 1),
      'every_direction': SensorConfiguration('every_direction', True, 3)
    },
    0,
    1,
    1)

  environment.add_agent(human_agent)

  environment.print_discovered_map()

  execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  print('Action result:', execute_action_result.get_action_result())

  execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, DownDirectionalSensor.IDENTIFIER)
  print('Sensor result:', execute_sensor_result.get_sensor_result())

  environment.print_discovered_map()

  execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  print('Action result:', execute_action_result.get_action_result())

  print('--= Agent information =--')
  print(f'Position: ({human_agent.get_x()}, {human_agent.get_y()})')
  print(f'Direction: {human_agent.get_direction()}')
  print(f'Steps: {human_agent.get_steps()}')
  print(f'Accumulated Movement Cost: {human_agent.get_accumulated_movement_cost()}')
  print('--= ----- =--')

  environment.print_discovered_map()

  execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, 'every_direction')
  print('Sensor result:', execute_sensor_result.get_sensor_result())

  environment.print_discovered_map()

  execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveRightAction.IDENTIFIER)
  print('Action result:', execute_action_result.get_action_result())

  print('--= Agent information =--')
  print(f'Position: ({human_agent.get_x()}, {human_agent.get_y()})')
  print(f'Direction: {human_agent.get_direction()}')
  print(f'Steps: {human_agent.get_steps()}')
  print(f'Accumulated Movement Cost: {human_agent.get_accumulated_movement_cost()}')
  print('--= ----- =--')

  environment.print_discovered_map()

  execute_sensor_result: ExecuteSensorResult = environment_agent_service.execute_sensor(human_agent, environment, 'every_direction')
  print('Sensor result:', execute_sensor_result.get_sensor_result())

  environment.print_discovered_map()
