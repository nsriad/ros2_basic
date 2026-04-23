import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class NumberPublisher2(Node):
    def __init__(self):
        super().__init__('number_publisher2')

        # publisher
        self.publisher_ = self.create_publisher(Int32, 'number2', 10)  # here queue size is 10
        # timer to publish every second
        self.timer = self.create_timer(1.0, self.publish_number)
        self.number = 1

    def publish_number(self):
        msg = Int32()
        msg.data = self.number
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing from node2: {msg.data}')
        self.number += 1

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher2()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
