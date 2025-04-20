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
        self.model = mujoco.MjModel.from_xml_path('robosoccer_sample.xml')
        self.data = mujoco.MjData(self.model)
        self.timer = self.create_timer(0.01, self.sim_step)  # 100 Hz
        self.get_logger().info('MuJoCo simulation running')

    def joint_command_callback(self, msg):
        # TODO: Parse and apply joint commands to self.data.ctrl
        pass

    def sim_step(self):
        mujoco.mj_step(self.model, self.data)
        # Publish dummy joint states
        js = JointState()
        js.name = [f'joint_{i}' for i in range(self.model.nq)]
        js.position = self.data.qpos.tolist()
        js.velocity = self.data.qvel.tolist()
        self.joint_state_pub.publish(js)
        # Publish dummy IMU
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
