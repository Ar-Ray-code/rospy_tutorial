# http://wiki.ros.org/noetic/Installation/Ubuntu

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -

sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

sudo rosdep init
rosdep update

mkdir -p ~/ros1_ws/src
source /opt/ros/noetic/setup.bash
cd ~/ros1_ws/src && catkin_init_workspace

echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
echo "source ~/ros1_ws/devel/setup.bash" >> ~/.bashrc

