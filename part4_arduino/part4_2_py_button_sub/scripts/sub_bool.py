#!/bin/python3
import rospy
from std_msgs.msg import Bool

class hello_world:
    def __init__(self):
        rospy.Subscriber('pushed',Bool,self.sub_number)
        rospy.spin()
    
    def sub_number(self,data):
        rospy.loginfo(str(data.data))

def rospy_init(args = None):
    rospy.init_node('sub_node',argv=args)
    hello_world()

if __name__=="__main__":
    rospy_init()