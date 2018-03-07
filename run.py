from tests.input import inputs

TYPE_AIR = 'air'
TYPE_GROUND = 'ground'


for input in inputs:
    current_pos = input['initial_pos']
    current_direction = input['initial_dir']

    print('Type - ' + input['type'])
    print('INITIAL_LOCATION')
    print('DIRECTION - ' + current_direction)
    print(current_pos)


    directions = ['N', 'E', 'S', 'W']
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for step in input['command']:
        curr_dir_index = (directions.index(current_direction))
        if step == 'R':
            current_direction = directions[(curr_dir_index + 1) % 4]
        elif step == 'L':
                current_direction = directions[(curr_dir_index - 1) % 4]
        elif step == 'F':
                current_pos[0] = current_pos[0] + move[curr_dir_index][0]
                current_pos[1] = current_pos[1] + move[curr_dir_index][1]

        if input['type'] == TYPE_AIR:
            if step == 'U':
                current_pos[2] = current_pos[2] + 10
            elif step == 'D':
                current_pos[2] = current_pos[2] - 10


    print('CURRENT_LOCATION')
    print('DIRECTION - ' + current_direction)
    print(current_pos)
    print('------------------')


