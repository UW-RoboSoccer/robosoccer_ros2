#JointCommand.msg - message definition for joint commands
float64[] position  # Target position for each joint in radians
float64[] velocity  # Target velocity for each joint in radians per second
float64[] effort    # Target effort for each joint in Newton-meters