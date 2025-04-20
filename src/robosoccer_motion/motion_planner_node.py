import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class MotionPlannerNode(Node):
    def __init__(self):
        super().__init__('motion_planner_node')
        self.create_subscription(String, '/behavior_state', self.behavior_callback, 10)
        self.footsteps_pub = self.create_publisher(String, '/footsteps', 10)  # TODO: Replace String with custom msg
        self.target_pose_pub = self.create_publisher(PoseStamped, '/target_pose', 10)
        # TODO: Implement footstep and kick planning

    def behavior_callback(self, msg):
        # TODO: Plan footsteps and kicks
        pass

def main(args=None):
    rclpy.init(args=args)
    node = MotionPlannerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
