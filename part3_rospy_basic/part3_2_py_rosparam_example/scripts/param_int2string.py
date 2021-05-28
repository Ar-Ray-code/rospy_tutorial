#!/bin/python3
import rospy

class param_int2string:
    def __init__(self):

        self.number = rospy.get_param("~get_number", -1)
        rospy.set_param("~set_number2str",str(self.number))
        rospy.set_param("set_number2str",str(self.number))
        self.pub_number()
    
    def pub_number(self):
        while not rospy.is_shutdown():
            rospy.loginfo(str(self.number))
            rospy.loginfo("exit")
            exit(0)

# print("Usage : '$ rosrun rosparam_example param_int2string.py _get_number:=300'")
def rospy_init(args = None):
    rospy.init_node('pub_node',argv=args)
    param_int2string()
    
if __name__=="__main__":
    rospy_init()