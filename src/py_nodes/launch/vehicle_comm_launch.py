import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    rviz_config = os.path.join(
    get_package_share_directory('py_nodes'),
    'rviz',
    'vehicle_visualization.rviz'
    )

    return LaunchDescription([
        Node(package='py_nodes', executable='vehicle1', name='vehicle1_node'),
        Node(package='py_nodes', executable='vehicle2', name='vehicle2_node'),
        Node(package='rviz2', executable='rviz2', name='rviz2', arguments=['-d', rviz_config]),
    ])