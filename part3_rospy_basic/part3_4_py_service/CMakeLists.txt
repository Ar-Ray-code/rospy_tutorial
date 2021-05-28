cmake_minimum_required(VERSION 3.0.2)
project(part3_4_py_service)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  original_msg_srv
)