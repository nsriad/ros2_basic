cmake_minimum_required(VERSION 3.8)
project(cpp_nodes)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(number_publisher1 src/number_publisher1.cpp)
ament_target_dependencies(number_publisher1 rclcpp std_msgs)

add_executable(number_publisher2 src/number_publisher2.cpp)
ament_target_dependencies(number_publisher2 rclcpp std_msgs)

add_executable(multiplier_node src/multiplier_node.cpp)
ament_target_dependencies(multiplier_node rclcpp std_msgs)

install(TARGETS
  number_publisher1
  number_publisher2
  multiplier_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
