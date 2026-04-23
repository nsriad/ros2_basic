# ROS2 Multiplication System (Python)

This project implements a simple ROS2 system using the publish–subscribe model.  
Two nodes publish integer values, and one node subscribes to both topics and multiplies the received values.

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
     └── py_nodes/
         ├── number_publisher1.py
         ├── number_publisher2.py
         ├── multiplier_node.py

```
---

## Requirements

- ROS2 Humble
- Python 3
- rclpy
- std_msgs

---

## Build

cd ~/ros2_basic  
colcon build  
source install/setup.bash  

---

## Run

Open three terminals.

Terminal 1:
ros2 run py_nodes number_pub1  

Terminal 2:
ros2 run py_nodes number_pub2  

Terminal 3:
ros2 run py_nodes multiplier  

---

## Example Output

Multiply: 100 x 11 = 1100  
Multiply: 105 x 12 = 1260  
Multiply: 110 x 13 = 1430  

---

## Notes

- Each terminal must source the workspace before running nodes
- Message timing between topics is not synchronized
- Output order may vary depending on execution timing

---

## Next Steps

- Implement the same system in C++


