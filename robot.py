class Robot(object):

    TYPE_AIR = 'air'
    TYPE_GROUND = 'ground'
    directions = ['N', 'E', 'S', 'W']
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def __init__(self , type, pos, dir):
        self.robot_type = type
        self.pos = pos
        self.dir = dir


    def move(self, command):
        current_pos = self.pos
        current_direction = self.dir

        for step in command:
            curr_dir_index = self.directions.index(current_direction)
            if step == 'R':
                current_direction = self.directions[(curr_dir_index + 1) % 4]
            elif step == 'L':
                current_direction = self.directions[(curr_dir_index - 1) % 4]
            elif step == 'F':
                current_pos[0] = current_pos[0] + self.moves[curr_dir_index][0]
                current_pos[1] = current_pos[1] + self.moves[curr_dir_index][1]

            # For AIR robots this will be the case
            # Increase or decrease Z by 10
            if self.robot_type == self.TYPE_AIR:
                if step == 'U':
                    current_pos[2] = current_pos[2] + 10
                elif step == 'D':
                    current_pos[2] = current_pos[2] - 10

        self.pos = current_pos
        self.dir = current_direction


    def get_current_position(self):
        return  self.pos

    def get_current_direction(self):
        return self.dir

    def print_current_location(self):
        print('Type - ' + self.robot_type)
        print('CURRENT_LOCATION')
        print('DIRECTION - ' + self.dir)
        print(self.pos)
