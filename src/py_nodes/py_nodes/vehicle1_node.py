import math

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, TransformStamped
from tf2_ros import TransformBroadcaster
from visualization_msgs.msg import Marker


class Vehicle1Node(Node):
    def __init__(self):
        super().__init__('vehicle1_node')

        # publish own velocity
        self.publisher_ = self.create_publisher(Twist, '/vehicle1/velocity', 10)

        # publish vehicle shape for rviz
        self.marker_publisher = self.create_publisher(Marker, '/vehicle1/marker', 10)

        # subscribe to vehicle 2 velocity
        self.subscription = self.create_subscription(Twist, '/vehicle2/velocity', self.vehicle2_callback, 10)
        # tf broadcaster
        self.tf_broadcaster = TransformBroadcaster(self)

        # initial forward velocity
        self.velocity = 0.2

        # vehicle pose in map frame
        self.x = 0.0
        self.y = 0.0
        self.yaw = 0.0
        self.dt = 1.0

        # publish every 1 second
        self.timer = self.create_timer(self.dt, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = self.velocity
        msg.angular.z = 0.1

        self.publisher_.publish(msg)
        self.get_logger().info(f'vehicle 1 publishing: linear.x={msg.linear.x}, angular.z={msg.angular.z}')

        self.velocity += 0.0  # keep constant velocity for simplicity

        # update simple vehicle position
        self.x += self.velocity * self.dt

        # broadcast transform from map to vehicle1/base_link
        transform = TransformStamped()
        transform.header.stamp = self.get_clock().now().to_msg()
        transform.header.frame_id = 'map'
        transform.child_frame_id = 'vehicle1/base_link'

        transform.transform.translation.x = self.x
        transform.transform.translation.y = self.y
        transform.transform.translation.z = 0.0

        qz = math.sin(self.yaw / 2.0)
        qw = math.cos(self.yaw / 2.0)

        transform.transform.rotation.x = 0.0
        transform.transform.rotation.y = 0.0
        transform.transform.rotation.z = qz
        transform.transform.rotation.w = qw

        self.tf_broadcaster.sendTransform(transform)

        # publish simple vehicle marker
        marker = Marker()
        marker.header.frame_id = 'map'
        marker.header.stamp = self.get_clock().now().to_msg()
        # marker.frame_locked = True

        marker.ns = 'vehicle1'
        marker.id = 1
        marker.type = Marker.CUBE
        marker.action = Marker.ADD

        marker.pose.position.x = self.x
        marker.pose.position.y = self.y
        marker.pose.position.z = 0.5

        marker.pose.orientation.x = 0.0
        marker.pose.orientation.y = 0.0
        marker.pose.orientation.z = qz
        marker.pose.orientation.w = qw

        marker.scale.x = 0.5
        marker.scale.y = 0.25
        marker.scale.z = 0.2

        marker.color.r = 1.0
        marker.color.g = 0.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        self.marker_publisher.publish(marker)

    def vehicle2_callback(self, msg):
        self.get_logger().info(f'vehicle 1 received vehicle 2 velocity: linear.x={msg.linear.x}, angular.z={msg.angular.z}')


def main(args=None):
    rclpy.init(args=args)

    node = Vehicle1Node()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
