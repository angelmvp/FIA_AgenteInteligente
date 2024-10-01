from src.agent.domain.action.action_repository import ActionRepository
from src.agent.domain.action.action_configuration import ActionConfiguration
from src.agent.domain.action.move_down_action import MoveDownAction
from src.agent.domain.action.move_left_action import MoveLeftAction
from src.agent.domain.action.move_right_action import MoveRightAction
from src.agent.domain.action.move_up_action import MoveUpAction
from src.agent.domain.agent import Agent
from src.agent.domain.sensor.down_directional_sensor import DownDirectionalSensor
from src.agent.domain.sensor.left_directional_sensor import LeftDirectionalSensor
from src.agent.domain.sensor.right_directional_sensor import RightDirectionalSensor
from src.agent.domain.sensor.sensor_configuration import SensorConfiguration
from src.agent.domain.sensor.sensor_repository import SensorRepository
from src.agent.domain.sensor.up_directional_sensor import UpDirectionalSensor
from src.environment.application.environment_agent_service import EnvironmentAgentService, ExecuteActionResult, ResultCode
from src.environment.application.environment_service import EnvironmentService
from src.environment.domain.environment import Environment
from src.environment.domain.terrain.terrain_repository import TerrainRepository
from src.map.domain.map import Map
from src.map.domain.map_repository import MapRepository

if __name__ == '__main__':
  terrain_repository: TerrainRepository = TerrainRepository('../resources/terrain')
  terrain_repository.load_from_file('terrain.json')

  map_repository: MapRepository = MapRepository('../resources/map')
  maze_map: Map = map_repository.load('maze.csv')
  maze_map.print()

  environment_service: EnvironmentService = EnvironmentService(terrain_repository)
  environment: Environment = environment_service.create_environment_from_map(maze_map)

  action_repository: ActionRepository = ActionRepository()
  action_repository.add_actions(MoveUpAction(), MoveDownAction(), MoveLeftAction(), MoveRightAction())

  sensor_repository: SensorRepository = SensorRepository()
  sensor_repository.add_sensors(UpDirectionalSensor(), DownDirectionalSensor(), LeftDirectionalSensor(), RightDirectionalSensor())

  environment_agent_service: EnvironmentAgentService = EnvironmentAgentService(action_repository, sensor_repository)

  known_map = [[None for _ in range(maze_map.get_rows())] for _ in range(maze_map.get_columns())]
  human_agent = Agent(
    0,
    {
      MoveUpAction.IDENTIFIER: ActionConfiguration(MoveUpAction.IDENTIFIER, {'steps': 1}),
      MoveDownAction.IDENTIFIER: ActionConfiguration(MoveDownAction.IDENTIFIER, {'steps': 1}),
      MoveLeftAction.IDENTIFIER: ActionConfiguration(MoveLeftAction.IDENTIFIER, {'steps': 1}),
      MoveRightAction.IDENTIFIER: ActionConfiguration(MoveRightAction.IDENTIFIER, {'steps': 1})
    },
    None,
    known_map,
    'human',
    {
      UpDirectionalSensor.IDENTIFIER: SensorConfiguration(UpDirectionalSensor.IDENTIFIER, False, 1),
      DownDirectionalSensor.IDENTIFIER: SensorConfiguration(DownDirectionalSensor.IDENTIFIER, False, 1),
      LeftDirectionalSensor.IDENTIFIER: SensorConfiguration(LeftDirectionalSensor.IDENTIFIER, False, 1),
      RightDirectionalSensor.IDENTIFIER: SensorConfiguration(RightDirectionalSensor.IDENTIFIER, False, 1)
    },
    0,
    1,
    1)

  human_agent.set_known(1, 1)
  environment.update_discovered_map(1, 1, True)

  environment_service.print_discovered_map(environment)

  execute_action_result: ExecuteActionResult = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  print('Action result:', execute_action_result.get_action_result())

  execute_sensor_result = environment_agent_service.execute_sensor(human_agent, environment, DownDirectionalSensor.IDENTIFIER)
  print('Sensor result:', execute_sensor_result.get_sensor_result())

  execute_action_result = environment_agent_service.execute_action(human_agent, environment, MoveDownAction.IDENTIFIER)
  print('Action result:', execute_action_result.get_action_result())

  print(f'Agent position ({human_agent.get_x()}, {human_agent.get_y()})')

  environment_service.print_discovered_map(environment)
