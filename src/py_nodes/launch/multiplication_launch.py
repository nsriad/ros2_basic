from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='py_nodes',
            executable='number_pub1',
            name='number_publisher1'
        ),

        Node(
            package='py_nodes',
            executable='number_pub2',
            name='number_publisher2'
        ),

        Node(
            package='py_nodes',
            executable='multiplier',
            name='multiplier_node'
        ),
    ])