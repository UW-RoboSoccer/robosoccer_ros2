import mujoco
import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState, Imu
from std_msgs.msg import String
import json

class MujocoSimNode(Node):
    def __init__(self):
        super().__init__('mujoco_sim_node')
        self.joint_state_pub = self.create_publisher(JointState, '/joint_states', 10)
        self.imu_pub = self.create_publisher(Imu, '/imu/data', 10)
        self.create_subscription(String, '/joint_command', self.joint_command_callback, 10)
        
        # Load MuJoCo model
        xml_path = self.declare_parameter('xml_path', 'robosoccer_sample.xml').get_parameter_value().string_value
        self.model = mujoco.MjModel.from_xml_path(xml_path)
        self.data = mujoco.MjData(self.model)
        
        # Store joint names and actuator indices
        self.joint_names = [self.model.joint(i).name for i in range(self.model.njnt)]
        self.actuator_names = [self.model.actuator(i).name for i in range(self.model.nu)]
        self.joint_to_actuator = {name: i for i, name in enumerate(self.actuator_names)}
        
        # Initialize control array
        self.data.ctrl = np.zeros(self.model.nu)
        
        # Create timer for simulation steps
        self.timer = self.create_timer(0.01, self.sim_step)  # 100 Hz
        self.get_logger().info('MuJoCo simulation running')

    def joint_command_callback(self, msg):
        try:
            # Parse joint commands from JSON string
            commands = json.loads(msg.data)
            
            # Apply commands to actuators
            for joint_name, position in commands.items():
                if joint_name in self.joint_to_actuator:
                    actuator_idx = self.joint_to_actuator[joint_name]
                    self.data.ctrl[actuator_idx] = position
                else:
                    self.get_logger().warn(f'Unknown joint: {joint_name}')
        except json.JSONDecodeError:
            self.get_logger().error('Failed to parse joint commands JSON')
        except Exception as e:
            self.get_logger().error(f'Error in joint command callback: {str(e)}')

    def sim_step(self):
        # Step the simulation
        mujoco.mj_step(self.model, self.data)
        
        # Publish joint states
        js = JointState()
        js.header.stamp = self.get_clock().now().to_msg()
        js.name = self.joint_names
        js.position = self.data.qpos.tolist()
        js.velocity = self.data.qvel.tolist()
        self.joint_state_pub.publish(js)
        
        # Publish IMU data from simulation
        imu = Imu()
        imu.header.stamp = self.get_clock().now().to_msg()
        imu.header.frame_id = 'imu_link'
        
        # Get base link orientation and angular velocity
        base_quat = self.data.sensordata[4:8]  # framequat sensor
        base_ang_vel = self.data.sensordata[8:11]  # frameangvel sensor
        base_lin_vel = self.data.sensordata[2:5]  # framelinvel sensor
        
        # Set IMU data
        imu.orientation.x = float(base_quat[0])
        imu.orientation.y = float(base_quat[1])
        imu.orientation.z = float(base_quat[2])
        imu.orientation.w = float(base_quat[3])
        
        imu.angular_velocity.x = float(base_ang_vel[0])
        imu.angular_velocity.y = float(base_ang_vel[1])
        imu.angular_velocity.z = float(base_ang_vel[2])
        
        # Approximate linear acceleration from velocity differences
        if not hasattr(self, 'prev_lin_vel'):
            self.prev_lin_vel = base_lin_vel
            self.prev_time = self.get_clock().now()
        else:
            current_time = self.get_clock().now()
            dt = (current_time - self.prev_time).nanoseconds / 1e9
            if dt > 0:
                accel = (base_lin_vel - self.prev_lin_vel) / dt
                imu.linear_acceleration.x = float(accel[0])
                imu.linear_acceleration.y = float(accel[1])
                imu.linear_acceleration.z = float(accel[2])
            self.prev_lin_vel = base_lin_vel
            self.prev_time = current_time
        
        self.imu_pub.publish(imu)

def main(args=None):
    rclpy.init(args=args)
    node = MujocoSimNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
