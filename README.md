# ROS2 Multiplication System (Python and C++)

This project implements simple ROS2 publish–subscribe examples using Python and C++.

The first example is a multiplication system where two nodes publish integer values and one node subscribes to both topics to compute the product.

The second example is a simple vehicle-to-vehicle communication system where two vehicle nodes publish their own velocity and subscribe to each other's velocity topic.

---

## Overview

ROS2 systems are composed of independent nodes that communicate through topics.

- number_publisher1 publishes to /number1
- number_publisher2 publishes to /number2
- multiplier_node subscribes to both and computes the product

Vehicle communication example:

- vehicle1_node publishes to /vehicle1/velocity
- vehicle2_node publishes to /vehicle2/velocity
- vehicle1_node subscribes to /vehicle2/velocity
- vehicle2_node subscribes to /vehicle1/velocity

The vehicle velocity is published using `geometry_msgs/msg/Twist`.

---

## Structure

```
ros2_basic/
└── src/
    └── py_nodes/
    |   ├── launch/
    |   │   ├── multiplication_launch.py
        |   └── vehicle_comm_launch.py
    |   └── py_nodes/
    |       ├── number_publisher1.py
    |       ├── number_publisher2.py
    |       ├── multiplier_node.py
    |       ├── vehicle1_node.py
    |       └── vehicle2_node.py
    │
    └── cpp_nodes/
        └── src/
            ├── number_publisher1.cpp
            ├── number_publisher2.cpp
            └── multiplier_node.cpp

```
---

## Requirements

- ROS2 Humble
- Python 3
- rclpy
- std_msgs
- geometry_msgs

For the C++ implementation:
- rclcpp
- CMake/ament_cmake

---

## Build

```bash
cd ~/ros2_basic  
colcon build  
source install/setup.bash  
```

---

## Run Python version

Open three terminals.

Terminal 1:
```bash 
ros2 run py_nodes number_pub1
```

Terminal 2:
```bash
ros2 run py_nodes number_pub2
```

Terminal 3:
```bash
ros2 run py_nodes multiplier 
```

## Run Python Version Using Launch File

The multiplication nodes can also be started together using a launch file:

```bash
ros2 launch py_nodes multiplication_launch.py
```

---

## Run C++ Version

Open three terminals.

Terminal 1:
```bash
ros2 run cpp_nodes number_publisher1
```

Terminal 2:
```bash
ros2 run cpp_nodes number_publisher2
```

Terminal 3:
```bash
ros2 run cpp_nodes multiplier_node
```

## Example Output

```
Multiply: 100 x 11 = 1100  
Multiply: 105 x 12 = 1260  
Multiply: 110 x 13 = 1430
```  

---


---

## Run Vehicle Communication Example

This example has two vehicle nodes. Each vehicle publishes its own velocity and subscribes to the other vehicle's velocity.

Run both vehicle nodes together using the launch file:

```bash
ros2 launch py_nodes vehicle_comm_launch.py
```

---

## Live Plot Using RQT

This project can also be visualized using `rqt_plot`. This allows us to see the published topic values changing live.

First, make sure the ROS2 workspace is sourced:

```bash
source install/setup.bash
```

Run the publisher nodes in separate terminals and then open `rqt_plot` with the topic values using following command:
```bash
ros2 run rqt_plot rqt_plot /number1/data /number2/data
```

For `rqt_graph` view:

```bash
ros2 run rqt_graph rqt_graph
```

For the vehicle communication example, plot the forward velocity of both vehicles:

```bash
ros2 run rqt_plot rqt_plot /vehicle1/velocity/linear/x /vehicle2/velocity/linear/x
```

---

## Notes

- Each terminal must source the workspace before running nodes
- Message timing between topics is not synchronized
- Output order may vary depending on execution timing
- `rqt_graph` can be used to view node and topic connections
- `rqt_plot` can be used to view topic values changing over time

---

## Next Steps

- Add more vehicle state information such as position and acceleration
- Extend the vehicle example to simulation tools such as CARLA
- Add C++ implementation for the vehicle communication example


