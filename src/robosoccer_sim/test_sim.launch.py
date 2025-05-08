from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Get the path to the test model
    package_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    xml_path = os.path.join(package_path, 'resource', 'test_model.xml')
    
    return LaunchDescription([
        Node(
            package='robosoccer_sim',
            executable='mujoco_sim_node',
            name='mujoco_sim_node',
            output='screen',
            parameters=[{'xml_path': xml_path}],
        ),
    ]) 