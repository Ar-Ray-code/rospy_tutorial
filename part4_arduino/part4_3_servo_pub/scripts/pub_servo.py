#!/bin/python3
import rospy
from std_msgs.msg import UInt16

class cmd_msg():

    def __init__(self):
        self.count = 0

        self.pub = rospy.Publisher('cmd_msg', UInt16, queue_size=1)
        hz = float(rospy.get_param("~pub_rate", 2))
        
        duraction = rospy.Duration(secs=0, nsecs=int(1/hz*1000000000))
        self.timer = rospy.Timer(duraction, self.pub_number)
        rospy.spin()
    
    def pub_number(self, dummy):
        angle = 0
        self.count = self.count + 1

        if(self.count == 0):
            angle = 0
        elif(self.count == 1):
            angle = 45
        elif(self.count == 2):
            angle = 90
        elif(self.count == 3):
            angle = 135
        elif(self.count == 4):
            angle = 180
        elif(self.count == 5):
            angle = 135
        elif(self.count == 6):
            angle = 90
        elif(self.count == 7):
            angle = 45
        elif(self.count == 8):
            angle = 0
            self.count = 0

        self.pub.publish(angle)

def ros_main(args = None):
    rospy.init_node('pub_node',argv=args)
    cmd_msg()

if __name__=="__main__":
    ros_main()