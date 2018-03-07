The ground vehicle can do the following:
- Turn right 90 degrees. - Turn left 90 degrees.
- Move forward 1 meter.

The airborne can do the following:
- Turn right 90 degrees.
- Turn left 90 degrees.
- Move forward 1 meter.
- Move higher by 10 meters. - Move lower by 10 meters.

This means the robot can move around on a grid, where each grid is 1m x 1m. We can assigns codes to the above commands:
- R: turn right.
- L: turn left.
- F: move forward. - U: move higher. - D: move lower.

This means we can send the robot the following string of commands: ground RFFFFLLFFFFRFFFF
or
air URFFFLLLUUUDDD

This moves the robots around the grid.

Finally, we can request that the robot tell us the direction it is facing, and which part of the grid it is on. It will tell us the x,y,z position of the coordinate, and whether it is facing N,E,S,W (north, east, south, or west)

For example, if we position the robot at the starting point on the bottom left hand corner of the grid (0,0) facing North, and issue the following command FFR, then the robot will report that its position is: 0,2 and its direction is E.

Create some code such that we can instantiate a robot, move it around and ask it for its position and direction. Input and output can be very basic, and no visualization is needed. You can even hard code some input and output for various cases.