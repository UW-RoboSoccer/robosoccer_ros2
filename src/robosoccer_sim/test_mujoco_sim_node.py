# Sample test for MujocoSimNode
import pytest
import rclpy
from robosoccer_sim.mujoco_sim_node import MujocoSimNode

def test_node_init():
    rclpy.init()
    node = MujocoSimNode()
    assert node.get_name() == 'mujoco_sim_node'
    node.destroy_node()
    rclpy.shutdown()
