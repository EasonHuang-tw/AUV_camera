#!/usr/bin/env python
import roslib
roslib.load_manifest('beginner_tutorials')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

def publish_cv():
  rospy.init_node('CV_convert_to_ROS_Image', anonymous=True)
  image_pub = rospy.Publisher("image_topic",Image, queue_size=20)
  bridge = CvBridge()
  rate = rospy.Rate(10) # 10hz
  while not rospy.is_shutdown():
    _, frame = cap.read()
    try:
      image_message = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
    except CvBridgeError as e:
      print(e)
    cv2.imshow("Image window", frame)
    rospy.loginfo(frame.shape)
    image_pub.publish(image_message)
    k = cv2.waitKey(5)
    rate.sleep()

if __name__ == '__main__':
  try:
    publish_cv()
  except KeyboardInterrupt:
    print("Shutting down")
    cv2.destroyAllWindows()
