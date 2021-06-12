#!/bin/python3
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class webcam_sub:
    def __init__(self):
        self.bridge = CvBridge()
        cv2.namedWindow("window",cv2.WINDOW_AUTOSIZE)     
        rospy.Subscriber("usb_cam/image_raw",Image,self.process_image)
    
    def __del__(self):
        cv2.destroyAllWindows()

    def process_image(self,msg):
        try:
            img_rgb = self.bridge.imgmsg_to_cv2(msg,"bgr8")
            cv2.putText(img_rgb, 'Test', (150, 150), cv2.FONT_HERSHEY_PLAIN, 10, (0, 255, 255), 5, cv2.LINE_AA)
            cv2.imshow("window", img_rgb)
            cv2.waitKey(1)
        except Exception as err:
            print(err)

def ros_main():
    rospy.init_node('put_text_sub')
    webcam_sub()
    rospy.spin()

if __name__ == "__main__":
    ros_main()
