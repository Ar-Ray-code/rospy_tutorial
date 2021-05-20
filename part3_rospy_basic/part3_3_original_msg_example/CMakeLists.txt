cmake_minimum_required(VERSION 3.0.2)
project(part3_3_original_msg_example)

set(CMAKE_CXX_FLAGS "-std=c++11 ${CMAKE_CXX_FLAGS}")

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)