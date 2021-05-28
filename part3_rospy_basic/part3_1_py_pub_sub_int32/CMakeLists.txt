cmake_minimum_required(VERSION 3.0.2)
project(part3_1_pub_sub_int32)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)
catkin_package()