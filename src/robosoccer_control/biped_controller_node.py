import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class BipedControllerNode(Node):
    def __init__(self):
        super().__init__('biped_controller_node')
        self.create_subscription(String, '/footsteps', self.footsteps_callback, 10)
        self.create_subscription(PoseStamped, '/target_pose', self.target_pose_callback, 10)
        self.joint_pub = self.create_publisher(String, '/joint_command', 10)  # TODO: Replace String with custom msg
        # TODO: Implement TSID/ZMP/whole-body control

    def footsteps_callback(self, msg):
        # TODO: Use footsteps for control
        pass

    def target_pose_callback(self, msg):
        # TODO: Use target pose for control
        pass

def main(args=None):
    rclpy.init(args=args)
    node = BipedControllerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
