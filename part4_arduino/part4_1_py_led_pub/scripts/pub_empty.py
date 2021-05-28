#!/bin/python3
import rospy
from std_msgs.msg import Empty

class toggle_led():
    def __init__(self):
        self.pub = rospy.Publisher('toggle_led', Empty, queue_size=1)
        hz = float(rospy.get_param("~pub_rate", 2))
        
        duraction = rospy.Duration(secs=0, nsecs=int(1/hz*1000000000))
        self.timer = rospy.Timer(duraction, self.pub_number)
        rospy.spin()
    
    def pub_number(self, dummy):
        self.pub.publish()

def ros_main(args = None):
    rospy.init_node('pub_node',argv=args)
    toggle_led()

if __name__=="__main__":
    ros_main()