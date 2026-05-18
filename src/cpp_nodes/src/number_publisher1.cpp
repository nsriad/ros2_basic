#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

#include <chrono>
#include <cstdlib>
#include <memory>

class NumberPublisher1 : public rclcpp::Node{
public:
    NumberPublisher1() : Node("number_publisher1"){
        // initialize the starting number
        number_ = 0;

        // create a publisher for the number1 topic
        publisher_ = this->create_publisher<std_msgs::msg::Int32>("number1", 10);

        // publish a new number every 1 second by calling publish_number() function
        timer_ = this->create_wall_timer(
            std::chrono::seconds(1),
            std::bind(&NumberPublisher1::publish_number, this)
        );
    }

private:
    void publish_number(){
        // create an integer message
        auto message = std_msgs::msg::Int32();
        message.data = number_;

        // show the published value in the terminal
        RCLCPP_INFO(this->get_logger(), "Publishing number1: %d", message.data);

        // publish the message
        publisher_->publish(message);

        // increase the number for the next publish
        number_ = number_ + 5;
    }

    int number_;
    rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char * argv[]){
    // start ROS 2 communication
    rclcpp::init(argc, argv);

    // create and run the node
    auto node = std::make_shared<NumberPublisher1>();
    rclcpp::spin(node);

    // stop ROS 2 communication
    rclcpp::shutdown();
    return 0;
}