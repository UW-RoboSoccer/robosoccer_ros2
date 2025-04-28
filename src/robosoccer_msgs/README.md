# robosoccer_msgs package for custom message definitions
# Place your .msg, .srv, .action files here

## Message Flow Example
1. Sensor Data Collection: The joint_state_publisher node collects joint states and publishes them as sensor_msgs/msg/JointState messages.​

2. State Estimation: The state estimation node processes the joint states and IMU data to estimate the robot's pose, publishing nav_msgs/msg/Odometry and geometry_msgs/msg/TransformStamped messages.​

3. TSID Processing: The TSID node subscribes to the odometry and joint state messages, computes the required control commands, and publishes sensor_msgs/msg/JointState or std_msgs/msg/Float64MultiArray messages.​

4. Actuation: The hardware interface node subscribes to the control command messages and sends the appropriate signals to the robot's actuators.​

5. Simulation: Subscribe to relevant messages and connect to visualizer (MuJoCo to simulate behaviour)