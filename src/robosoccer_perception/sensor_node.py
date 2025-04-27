import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, Imu
from geometry_msgs.msg import Vector3


from adafruit_extended_bus import ExtendedI2C as I2C
import adafruit_bno08x
from adafruit_bno08x.i2c import BNO08X_I2C

import time
from math import atan2, sqrt
from math import pi as PI


class SensorNode(Node):
    def __init__(self):
        super().__init__('sensor_node')
        self.image_pub = self.create_publisher(Image, '/camera/image_raw', 10)
        # TODO: Implement camera hardware integration


        ##---IMU Publisher---##
        self.imu_pub = self.create_publisher(Imu, '/imu/data', 10)
        self.euler_pub = self.create_publisher(Imu, '/imu/euler_ori', 10)

        #IMU state
        self.imu = None
        self.quat = [0.0, 0.0, 0.0, 0.0] #sensor quaternion x,y,z,w
        self.linear_accel = [0.0, 0.0, 0.0] #sensor linear acceleration x,y,z
        self.gyro = [0.0, 0.0, 0.0] #sensor gyro x,y,z
        self.euler = [0.0, 0.0, 0.0] #roll, pitch, yaw

        self.init_imu()
        self.create_timer(0.1, self.publish_imu_data)

    def init_imu(self):
        i2c = I2C(3)
        try:
            self.imu = BNO08X_I2C(i2c)
        except:
            self.get_logger().error("BNO085 not found, check wiring and power")
            raise Exception("Failed to connect to BNO085")
        
        self.imu.enable_feature(adafruit_bno08x.BNO_REPORT_ROTATION_VECTOR) #For orientation_quat and Euler (heading) data
        self.imu.enable_feature(adafruit_bno08x.BNO_REPORT_LINEAR_ACCELERATION) #Linear Acceleration data
        self.imu.enable_feature(adafruit_bno08x.BNO_REPORT_GYROSCOPE) #Gyroscope angular velocity data

        time.sleep(0.5) #Wait for the sensor to initialize

    def read_and_publish_imu(self):
        try:
            # Read raw sensor data
            self._gyro = list(self.imu.gyro)                        # deg/s
            self._accel = list(self.imu.linear_acceleration)       # m/s²
            self._quat = list(self.imu.quaternion)                 # x,y,z,w
            self._compute_euler()

            # Build IMU msg
            imu_msg = Imu()
            # Swap axes if needed to match robot frame conventions
            imu_msg.angular_velocity.x =  self._gyro[0] * (PI/180.0)
            imu_msg.angular_velocity.y = -self._gyro[1] * (PI/180.0)
            imu_msg.angular_velocity.z =  self._gyro[2] * (PI/180.0)

            imu_msg.linear_acceleration.x =  self._accel[0]
            imu_msg.linear_acceleration.y = -self._accel[1]
            imu_msg.linear_acceleration.z =  self._accel[2]

            # Orientation quaternion: sensor → robot frame
            imu_msg.orientation.x =  self._quat[0]
            imu_msg.orientation.y = -self._quat[1]
            imu_msg.orientation.z =  self._quat[2]
            imu_msg.orientation.w =  self._quat[3]

            imu_msg.header.stamp = self.get_clock().now().to_msg()
            imu_msg.header.frame_id = 'imu_link'

            # Build Euler orientation msg
            euler_msg = Vector3()
            euler_msg.x = self._euler[0]   # roll (deg)
            euler_msg.y = self._euler[1]   # pitch (deg)
            euler_msg.z = self._euler[2]   # yaw (deg)

            # Publish
            self.imu_pub.publish(imu_msg)
            self.euler_pub.publish(euler_msg)

        except Exception as e:
            self.get_logger().error(f'Failed to read/publish IMU: {e}\n{traceback.format_exc()}')

    def _compute_euler(self):
        # Convert quaternion (x,y,z,w) → roll, pitch, yaw (deg)
        x, y, z, w = self._quat

        # Roll
        sinr_cosp = 2.0 * (w * x + y * z)
        cosr_cosp = 1.0 - 2.0 * (x*x + y*y)
        roll = atan2(sinr_cosp, cosr_cosp)

        # Pitch
        sinp = sqrt(1 + 2.0 * (w * y - z * x))
        cosp = sqrt(1 - 2.0 * (w * y - z * x))
        pitch = atan2(sinp, cosp) - PI/2

        # Yaw
        siny_cosp = 2.0 * (w * z + x * y)
        cosy_cosp = 1.0 - 2.0 * (y*y + z*z)
        yaw = atan2(siny_cosp, cosy_cosp)

        # Convert to degrees, adjust yaw to [0,360)
        self._euler[0] = roll  * (180.0/PI)
        self._euler[1] = pitch * (180.0/PI)
        self._euler[2] = (yaw * (180.0/PI)) % 360.0

    # Add timer or callback for publishing sensor data

def main(args=None):
    rclpy.init(args=args)
    node = SensorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
