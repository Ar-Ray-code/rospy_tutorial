cmake_minimum_required(VERSION 3.0.2)
project(original_msg_srv)

set(CMAKE_CXX_FLAGS "-std=c++11 ${CMAKE_CXX_FLAGS}")

find_package(catkin REQUIRED
  COMPONENTS
    std_msgs
    message_generation
)

add_message_files(
  FILES
    ExampleMsg.msg
    PositionXY.msg
)

## using service
add_service_files(
  FILES
    CalcMsgSrv.srv
)

generate_messages(
  DEPENDENCIES
    std_msgs
)

catkin_package(
 CATKIN_DEPENDS
    std_msgs
)