import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class Vehicle2Node(Node):
    def __init__(self):
        super().__init__('vehicle2_node')

        # publish own velocity
        self.publisher_ = self.create_publisher(Twist, '/vehicle2/velocity', 10)

        # subscribe to vehicle 1 velocity
        self.subscription = self.create_subscription(Twist, '/vehicle1/velocity', self.vehicle1_callback, 10)

        # publish every 1 second
        self.timer = self.create_timer(1.0, self.publish_velocity)

        # initial forward velocity
        self.velocity = 3.0

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.velocity
        msg.angular.z = -0.1

        self.publisher_.publish(msg)
        self.get_logger().info(f'vehicle 2 publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}')

        self.velocity += 0.3

    def vehicle1_callback(self, msg):
        self.get_logger().info(f'vehicle 2 received vehicle 1 velocity: linear.x={msg.linear.x}, angular.z={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)

    node = Vehicle2Node()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
