#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

#include <chrono>
#include <cstdlib>
#include <memory>

using std::placeholders::_1;

class MultiplierNode : public rclcpp::Node{
public:
    MultiplierNode() : Node("multiplier_node"){
        // initialize the received numbers
        number1_ = 0;
        number2_ = 0;

        // create a subscriber for the number1 topic
        subscriber1_ = this->create_subscription<std_msgs::msg::Int32>("number1", 10, std::bind(&MultiplierNode::number1_callback, this, _1));

        // create a subscriber for the number2 topic
        subscriber2_ = this->create_subscription<std_msgs::msg::Int32>("number2", 10, std::bind(&MultiplierNode::number2_callback, this, _1));
    }

private:
    void number1_callback(const std_msgs::msg::Int32::SharedPtr msg){
        // store the latest number1 value
        number1_ = msg->data;

        // multiply using the latest received values
        multiply();
    }

    void number2_callback(const std_msgs::msg::Int32::SharedPtr msg){
        // store the latest number2 value
        number2_ = msg->data;

        // multiply using the latest received values
        multiply();
    }

    void multiply(){
        // calculate the multiplication result
        int result = number1_ * number2_;

        // show the result in the terminal
        RCLCPP_INFO(
            this->get_logger(),
            "Multiply: %d x %d = %d",
            number1_,
            number2_,
            result
        );
    }

    int number1_;
    int number2_;

    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscriber1_;
    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscriber2_;
};

int main(int argc, char * argv[]){
    // start ROS 2 communication
    rclcpp::init(argc, argv);

    // create and run the node
    auto node = std::make_shared<MultiplierNode>();
    rclcpp::spin(node);

    // stop ROS 2 communication
    rclcpp::shutdown();
    return 0;
}