# Part3：rospy_basic

Pub-Sub example.

## 1. Pub-Sub int32

### Usage

- Publisher only
  - Terminal 1：`$ roscore`
  - Terminal 2：`$ rosrun pub_sub_int32 pub_int.py`
  - Terminal 3：`$ rostopic echo /pub_int`

![part3_helloworld1_pub](images_for_readme/part3_helloworld1_pub.png)

- Publisher & Subscriber

  - Terminal 1：`$ roscore`
  - Terminal 2：`$ rosrun pub_sub_int32 pub_int.py`

  - Terminal 3：`$ rosrun pub_sub_int32 sub_int.py`

![part3_helloworld1_pub](images_for_readme/part3_helloworld1_sub.png)