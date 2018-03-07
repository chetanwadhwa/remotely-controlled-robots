This Code is written in Python3

create your virtualenv

activate it by this command

    $ source venv/bin/activate 

To run the given Program

    $ python run.py

To add any other test case go to tests/input.py and add in the following format

FOR GROUND VEHICLE


    {
        'type' : 'ground',
        'command' : 'RFFFFLLFFFFRFFFF',
        'initial_pos' : [0,0],
        'initial_dir' : 'N'
    }
    
 FOR AIRBORNE VEHICLE
 
     {
        'type' : 'air',
        'command' : 'URFFFLLLUUUDDD',
        'initial_pos': [0, 0, 0],
        'initial_dir': 'N'
    }
    
    
 You will get outputs like this for each test case
 
 
    Type - ground
    INITIAL_LOCATION
    DIRECTION - N
    [0, 0]
    CURRENT_LOCATION
    DIRECTION - N
    [0, 4]
    ------------------
    Type - air
    INITIAL_LOCATION
    DIRECTION - N
    [0, 0, 0]
    CURRENT_LOCATION
    DIRECTION - S
    [3, 0, 10]
    ------------------
