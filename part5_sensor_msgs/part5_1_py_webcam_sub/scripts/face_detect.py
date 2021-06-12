#!/bin/python3
import os
from os.path import expanduser
from urllib.request import urlretrieve

import cv2

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from original_msg_srv.msg import PositionXY

home = expanduser("~")

download_path = home+'/.cache/face_detector/face_tracking/'
WEIGHTS_URL = 'https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel'
WEIGHTS_PATH = download_path+'opencv_face_detector.caffemodel'
CONFIG_URL = 'https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt'
CONFIG_PATH = download_path+'deploy.prototxt'

class FaceDetector:
    def __init__(self):
        self.weights_url = rospy.get_param("~weights_url", WEIGHTS_URL)
        self.config_url = rospy.get_param("~config_url", CONFIG_URL)
        self.weights_path = rospy.get_param("~weights_path", WEIGHTS_PATH)
        self.config_path = rospy.get_param("~config_path", CONFIG_PATH)
        self.conf_threshold = rospy.get_param("~threshold", 0.3)

        if not os.path.isfile(self.weights_path) or not os.path.isfile(self.config_path):
            urlretrieve(self.weights_url, self.weights_path)
            urlretrieve(self.config_url, self.config_path)

        self.net = cv2.dnn.readNetFromCaffe(self.config_path, self.weights_path)

    def process_image(self, image):
        blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), [104, 117, 123], False, False)
        self.net.setInput(blob)
        detections = self.net.forward()
        
        out_detections = []
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if confidence > self.conf_threshold:
                xmin = int(detections[0, 0, i, 3] * image.shape[1])
                ymin = int(detections[0, 0, i, 4] * image.shape[0])
                xmax = int(detections[0, 0, i, 5] * image.shape[1])
                ymax = int(detections[0, 0, i, 6] * image.shape[0])
                out_detections.append([xmin, ymin, xmax, ymax])
            
        return out_detections

class face_detect:
    def __init__(self):
        self.cvdnn_detector = FaceDetector()
        self.bridge = CvBridge()

        self.width = rospy.get_param("~frame_size/width", 360)
        self.height = rospy.get_param("~frame_size/height", 240)
        self.imshow_isview = rospy.get_param("~imshow_isshow", 1)
        
        self.pub_image = rospy.Publisher("output",Image,queue_size=1)
        rospy.Subscriber("usb_cam/image_raw",Image,self.process_image_ros1)
        self.pub_position = rospy.Publisher('face_position', PositionXY, queue_size=1)

    def process_image_ros1(self, msg):
        position = PositionXY()
        try:
            frame = self.bridge.imgmsg_to_cv2(msg,"bgr8")
            frame = cv2.resize(frame, dsize=(self.width,self.height))
            self.pub_image.publish(self.bridge.cv2_to_imgmsg(frame,"bgr8"))

            detections = self.cvdnn_detector.process_image(frame)
            if(detections):
                position.x = (detections[0][0] + detections[0][1]) //2
                position.y = (detections[0][2] + detections[0][3]) //2
            
            self.pub_position.publish(position)

            if self.imshow_isview:
                for det in detections:
                    cv2.rectangle(frame, (det[0], det[1]), (det[2], det[3]), (0, 255, 0))
                cv2.imshow('frame', frame)
                cv2.waitKey(1)

        except Exception as err:
            print(err)

def ros_main():
    rospy.init_node('face_detector')
    os.makedirs(download_path, exist_ok=True)
    face_detect()
    rospy.spin()

if __name__ == "__main__":
    ros_main()