#!/bin/python3
import rospy
from std_msgs.msg import Int32

class pub_int():
    def __init__(self):
        self.number = 0

        self.pub = rospy.Publisher('pub_int', Int32, queue_size=1)
        hz = float(rospy.get_param("~pub_rate", 2))
        
        duraction = rospy.Duration(secs=0, nsecs=int(1/hz*1000000000))
        self.timer = rospy.Timer(duraction, self.pub_number)
        rospy.spin()
    
    def pub_number(self, dummy):
        self.pub.publish(self.number)
        self.number = self.number + 1

def ros_main(args = None):
    rospy.init_node('pub_node',argv=args)
    pub_int()

if __name__=="__main__":
    ros_main()