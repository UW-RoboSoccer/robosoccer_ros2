from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robosoccer_sim',
            executable='mujoco_sim_node',
            name='mujoco_sim_node',
            output='screen',
            parameters=[{'xml_path': 'robosoccer_sample.xml'}],
        ),
        # Add other nodes to connect to simulation as needed
    ])
