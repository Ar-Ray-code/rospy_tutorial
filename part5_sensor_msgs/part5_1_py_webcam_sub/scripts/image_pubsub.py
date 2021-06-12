#!/bin/python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class image_pub_sub:
    def __init__(self):
        self.bridge = CvBridge()
        self.pub = rospy.Publisher("output_image",Image,queue_size=1)
        rospy.Subscriber("usb_cam/image_raw",Image,self.process_image)

    def process_image(self,msg):
        try:
            img_rgb = self.bridge.imgmsg_to_cv2(msg,"rgb8")
            cv2.putText(img_rgb, 'Test', (150, 150), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 255), 5, cv2.LINE_AA)
            
            output_img = self.bridge.cv2_to_imgmsg(img_rgb,"rgb8")
            self.pub.publish(output_img)
        except Exception as err:
            print(err)

def ros_main():
    rospy.init_node('img_pubsub')
    image_pub_sub()
    rospy.spin()

if __name__ == "__main__":
    ros_main()
