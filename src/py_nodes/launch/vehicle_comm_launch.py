from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='py_nodes', executable='vehicle1', name='vehicle1_node'),
        Node(package='py_nodes', executable='vehicle2', name='vehicle2_node'),
    ])