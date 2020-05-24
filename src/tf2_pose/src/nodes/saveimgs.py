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
from scipy.spatial.transform import Rotation as R
import message_filters
from sensor_msgs.msg import Image, CameraInfo

bridge = CvBridge()
colimg = 0
depimg = 0

def callback(col_im, dep_im, msg):
    global colimg
    global depimg
    cv_img_col = bridge.imgmsg_to_cv2(col_im, desired_encoding="bgr8")
    cv_img_dep = bridge.imgmsg_to_cv2(dep_im, desired_encoding="passthrough").astype(np.float32)
    print(msg)
    r = R.from_quat([msg.rotation.x, msg.rotation.y, msg.rotation.z, msg.rotation.w])
    transmatrix = np.eye(4,4)
    transmatrix[:3, :3] = r.as_dcm()
    transmatrix[0,3] = msg.translation.x
    transmatrix[1,3] = msg.translation.y
    transmatrix[2,3] = msg.translation.z
    colimg+=1
    if(colimg%5==0):
        cv2.imwrite('/home/olorin/Desktop/depthimgs/imags/color-%d.jpg'%(colimg), cv_img_col)
    depimg+=1
    if(depimg%5==0):
        np.save('/home/olorin/Desktop/depthimgs/imags/depth-%d.npy'%(depimg), cv_img_dep)
        np.save('/home/olorin/Desktop/depthimgs/pose-%d.npy'%(depimg), transmatrix)
        # cv_img_dep[cv_img_dep>1000] = 0
        # cv2.imwrite('/home/olorin/Desktop/depthimgs/imags/depth-%d.png'%(depimg), 20*cv_img_dep.astype(np.uint16))

    # print(cv_img_dep.shape)
    # print(campose)
  # Solve all of perception here...

# rospy.init_node('imagewrite')
# depth_image_topic = '/camera/depth/image_raw'
# color_image_topic = '/camera/color/image_raw'
# tftopic = '/cameraposetransform'

# color_image_sub = message_filters.Subscriber(color_image_topic, Image)
# depth_image_sub = message_filters.Subscriber(depth_image_topic, Image)



# ts = message_filters.TimeSynchronizer([color_image_sub, depth_image_sub], 10)
# ts.registerCallback(callback)
# rospy.spin()

def image_callback(msg):
    cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
    print(cv_img.shape)


def main():
    rospy.init_node('image_listener')
    color_image_topic = '/camera/color/image_raw'
    depth_image_topic = '/camera/depth/image_raw'
    tftopic = '/cameraposetransform'
    color_image_sub = message_filters.Subscriber(color_image_topic, Image)
    depth_image_sub = message_filters.Subscriber(depth_image_topic, Image)
    camera_pose_sub = message_filters.Subscriber(tftopic, geometry_msgs.msg.Transform)
    
    ts = message_filters.ApproximateTimeSynchronizer([color_image_sub, depth_image_sub, camera_pose_sub], 10, 0.1, allow_headerless=True)
    ts.registerCallback(callback)

    # Set up your subscriber and define its callback
    # rospy.Subscriber(depth_image_topic, Image, image_callback)
    # Spin until ctrl + c
    rospy.spin()

if __name__=='__main__':
    main()