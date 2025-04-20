import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped

class PerceptionNode(Node):
    def __init__(self):
        super().__init__('perception_node')
        self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.ball_pub = self.create_publisher(PoseStamped, '/ball_pose', 10)
        # TODO: Add perception logic (ball detection, etc)

    def image_callback(self, msg):
        # TODO: Process image and publish ball pose
        pass

def main(args=None):
    rclpy.init(args=args)
    node = PerceptionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
