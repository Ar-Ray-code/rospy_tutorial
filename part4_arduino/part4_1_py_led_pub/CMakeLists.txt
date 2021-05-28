cmake_minimum_required(VERSION 3.0.2)
project(part4_1_py_led_pub)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)
catkin_package()