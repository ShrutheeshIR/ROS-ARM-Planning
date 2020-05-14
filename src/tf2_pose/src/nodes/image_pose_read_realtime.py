#!/home/olorin/ENV/bin/python
import roslib
roslib.load_manifest('tf2_pose')
import rospy
import math
import tf
import geometry_msgs.msg
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np
import cv2
import os


def callback(data, bridge):
    try:
        cv_image = bridge.imgmsg_to_cv2(data, desired_encoding="passthrough").astype(np.float32)
    except CvBridgeError as e:
        print(e)

    (rows,cols) = cv_image.shape
    print(rows, cols)
        

def listener():
    bridge = CvBridge()
    listener = tf.TransformListener()
    image_sub = rospy.Subscriber("/camera/depth/image_raw",Image,callback, bridge)
    try:
        (trans,rot) = listener.lookupTransform('/world', '/camera_color_frame', rospy.Time(0))
        print(trans, rot)        
    except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        print("NO")





if __name__ == '__main__':
    rospy.init_node('tf_listener')
    listener()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")

