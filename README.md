# ROS2 Multiplication System (Python and C++)

This project implements a simple ROS2 system using the publish–subscribe model.  
Two nodes publish integer values, and one node subscribes to both topics and multiplies the received values.

The system is implemented in both Python and C++.

---

## Overview

ROS2 systems are composed of independent nodes that communicate through topics.

- number_publisher1 publishes to /number1
- number_publisher2 publishes to /number2
- multiplier_node subscribes to both and computes the product

---

## Structure

```
ros2_basic/
└── src/
    ├── py_nodes/
    │   └── py_nodes/
    │       ├── number_publisher1.py
    │       ├── number_publisher2.py
    │       └── multiplier_node.py
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

---

## Notes

- Each terminal must source the workspace before running nodes
- Message timing between topics is not synchronized
- Output order may vary depending on execution timing

---

## Next Steps

- Add launch files to run all nodes together


