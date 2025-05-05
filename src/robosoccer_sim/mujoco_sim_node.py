import mujoco
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState, Imu
from std_msgs.msg import String

class MujocoSimNode(Node):
    def __init__(self):
        super().__init__('mujoco_sim_node')
        self.joint_state_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.imu_pub = self.create_publisher(Imu, '/imu/data', 10)
        self.create_subscription(String, '/joint_command', self.joint_command_callback, 10)
        # Load MuJoCo model
        # Get XML path from ROS2 parameter or default
        xml_path = self.declare_parameter('xml_path', 'robosoccer_sample.xml').get_parameter_value().string_value
        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data = mujoco.MjData(self.model)
        # Store joint names from Mujoco actuators for publishing
        self.joint_names = [self.model.joint(i).name for i in range(self.model.njnt)]
        self.timer = self.create_timer(0.01, self.sim_step)  # 100 Hz
        self.get_logger().info('MuJoCo simulation running')

    def joint_command_callback(self, msg):
        # TODO: Parse and apply joint commands to self.data.ctrl
        # Example: msg.data should be a string or custom message with joint commands
        # You may want to use a more structured message (e.g., JointState or Float64MultiArray)
        pass

    def sim_step(self):
        mujoco.mj_step(self.model, self.data)
        # Publish joint states from Mujoco
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = self.joint_names
        js.position = self.data.qpos.tolist()
        js.velocity = self.data.qvel.tolist()
        self.joint_state_pub.publish(js)
        # Publish dummy IMU (replace with real data if available)
        imu = Imu()
        imu.header.stamp = self.get_clock().now().to_msg()
        imu.linear_acceleration.x = float(np.random.randn())
        imu.linear_acceleration.y = float(np.random.randn())
        imu.linear_acceleration.z = float(np.random.randn())
        self.imu_pub.publish(imu)

def main(args=None):
    rclpy.init(args=args)
    node = MujocoSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
