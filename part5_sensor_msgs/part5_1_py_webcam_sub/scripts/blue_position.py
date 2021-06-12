#!/bin/python3
import rospy
from sensor_msgs.msg import Image
from original_msg_srv.msg import PositionXY

import cv2
from cv_bridge import CvBridge
import numpy as np

imshow_isview = 1

class blue_position:
    def detect_blue(self, input_image)->list:
        hsv = cv2.cvtColor(input_image, cv2.COLOR_RGB2HSV)

        hsv_min = np.array([90, 64, 0])
        hsv_max = np.array([150,255,255])
        mask = cv2.inRange(hsv, hsv_min, hsv_max)

        M = cv2.moments(mask, False)
        x,y= int(M["m10"]/M["m00"]) , int(M["m01"]/M["m00"])

        if imshow_isview:
            masked_img = cv2.bitwise_and(input_image, input_image, mask=mask)
            masked_img = cv2.circle(masked_img,(x,y), 10, (0,255,0), -1)
            output = cv2.cvtColor(masked_img, cv2.COLOR_RGB2BGR)

            cv2.imshow("window", output)
            cv2.waitKey(1)

        return [x,y]

class position_pub(blue_position):
    def __init__(self):
        self.position_pub = rospy.Publisher("position",PositionXY,queue_size=1)
        self.bridge = CvBridge()

        if imshow_isview:
            cv2.namedWindow("window",cv2.WINDOW_AUTOSIZE)

        rospy.Subscriber("usb_cam/image_raw",Image,self.process_image)

    def __del__(self):
        cv2.destroyAllWindows()

    def process_image(self,msg):
        try:
            position_msg = PositionXY()
            img_rgb = self.bridge.imgmsg_to_cv2(msg,"rgb8")

            position_msg.x, position_msg.y = self.detect_blue(img_rgb)

            self.position_pub.publish(position_msg)
        except Exception as err:
            print(err)

def ros_main():
    rospy.init_node('put_text_pubsub')
    position_pub()
    rospy.spin()

if __name__ == "__main__":
    ros_main()
