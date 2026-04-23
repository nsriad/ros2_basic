import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32


class MultiplierNode(Node):
    def __init__(self):
        super().__init__('multiplier_node')
        self.num1 = None
        self.num2 = None
        self.sub1 = self.create_subscription(
            Int32,
            'number1',
            self.callback1,
            10
        )

        self.sub2 = self.create_subscription(
            Int32,
            'number2',
            self.callback2,
            10
        )

    def callback1(self, msg):
        self.num1 = msg.data
        self.compute()

    def callback2(self, msg):
        self.num2 = msg.data
        self.compute()

    def compute(self):
        if self.num1 is not None and self.num2 is not None:
            result = self.num1 * self.num2
            self.get_logger().info(
                f'Multiply: {self.num1} x {self.num2} = {result}'
            )
            self.num1 = None
            self.num2 = None


def main(args=None):
    rclpy.init(args=args)
    node = MultiplierNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()