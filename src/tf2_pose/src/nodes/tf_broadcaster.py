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



if __name__ == '__main__':
    rospy.init_node('tf_listener')
    print("YAY")
    bridge = CvBridge()

    listener = tf.TransformListener()
    # t = geometry_msgs.msg
    # r = geometry_msgs.msg.transform.rotation
    # print(t)
    # return [t.x, t.y, t.z], [r.x, r.y, r.z, r.w]

    # rospy.wait_for_service('spawn')
    # spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    # spawner(4, 2, 0, 'turtle2')

    transformer = rospy.Publisher('/cameraposetransform', geometry_msgs.msg.Transform,queue_size=1)

    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/world', '/camera_depth_optical_frame', rospy.Time(0))
            msg1 = geometry_msgs.msg.Transform()
            msg1.translation.x = trans[0]
            msg1.translation.y = trans[1]
            msg1.translation.z = trans[2]
            msg1.rotation.x = rot[0]
            msg1.rotation.y = rot[1]
            msg1.rotation.z = rot[2]
            msg1.rotation.w = rot[3]
            transformer.publish(msg1)
            # print(msg1)
            # print("#")
            # print(type(vaaal[0]))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            # print("NO")
            continue

        

        rate.sleep()
