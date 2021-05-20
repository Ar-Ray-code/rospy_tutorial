#!/bin/bash

SCRIPT_DIR=$(cd $(dirname $0); pwd)

sudo apt install ros-noetic-rosserial-arduino
sudo apt install ros-noetic-rosserial

mkdir $SCRIPT_DIR/arduino/blink
mkdir $SCRIPT_DIR/arduino/button
mkdir $SCRIPT_DIR/arduino/servo

wget -O $SCRIPT_DIR/arduino/blink/blink.ino https://raw.githubusercontent.com/ros-drivers/rosserial/noetic-devel/rosserial_arduino/src/ros_lib/examples/Blink/Blink.pde
wget -O $SCRIPT_DIR/arduino/button/button.ino https://raw.githubusercontent.com/ros-drivers/rosserial/noetic-devel/rosserial_arduino/src/ros_lib/examples/button_example/button_example.pde
wget -O $SCRIPT_DIR/arduino/servo/servo.ino https://raw.githubusercontent.com/ros-drivers/rosserial/noetic-devel/rosserial_arduino/src/ros_lib/examples/ServoControl/ServoControl.pde
