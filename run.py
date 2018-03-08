from tests.input import inputs
from robot import Robot



for input in inputs:

    robot = Robot(input['type'], input['initial_pos'], input['initial_dir'])

    robot.print_current_location()

    print('\nRUNNING_COMMAND : ')
    print(input['command'] + '\n')

    robot.move(input['command'])

    robot.print_current_location()

    print('----------------------------------')

