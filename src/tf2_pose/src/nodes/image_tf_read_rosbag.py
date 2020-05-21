
import os
import argparse
import numpy as np
import cv2
import tf
import rosbag
from sensor_msgs.msg import Image
import geometry_msgs.msg
from cv_bridge import CvBridge
import rospy
import transformations
from scipy.spatial.transform import Rotation as R
import open3d as o3d
import matplotlib.pyplot as plt


import tf.transformations as tr

from geometry_msgs.msg import Point
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import Transform
from geometry_msgs.msg import TransformStamped
from geometry_msgs.msg import Vector3

import numpy as np

def pose_to_pq(msg):
    """Convert a C{geometry_msgs/Pose} into position/quaternion np arrays

    @param msg: ROS message to be converted
    @return:
      - p: position as a np.array
      - q: quaternion as a numpy array (order = [x,y,z,w])
    """
    p = np.array([msg.position.x, msg.position.y, msg.position.z])
    q = np.array([msg.orientation.x, msg.orientation.y,
                  msg.orientation.z, msg.orientation.w])
    return p, q


def pose_stamped_to_pq(msg):
    """Convert a C{geometry_msgs/PoseStamped} into position/quaternion np arrays

    @param msg: ROS message to be converted
    @return:
      - p: position as a np.array
      - q: quaternion as a numpy array (order = [x,y,z,w])
    """
    return pose_to_pq(msg.pose)


def transform_to_pq(msg):
    """Convert a C{geometry_msgs/Transform} into position/quaternion np arrays

    @param msg: ROS message to be converted
    @return:
      - p: position as a np.array
      - q: quaternion as a numpy array (order = [x,y,z,w])
    """
    p = np.array([msg.translation.x, msg.translation.y, msg.translation.z])
    q = np.array([msg.rotation.x, msg.rotation.y,
                  msg.rotation.z, msg.rotation.w])
    return p, q


def transform_stamped_to_pq(msg):
    """Convert a C{geometry_msgs/TransformStamped} into position/quaternion np arrays

    @param msg: ROS message to be converted
    @return:
      - p: position as a np.array
      - q: quaternion as a numpy array (order = [x,y,z,w])
    """
    return transform_to_pq(msg.transform)


def msg_to_se3(msg):
    """Conversion from geometric ROS messages into SE(3)

    @param msg: Message to transform. Acceptable types - C{geometry_msgs/Pose}, C{geometry_msgs/PoseStamped},
    C{geometry_msgs/Transform}, or C{geometry_msgs/TransformStamped}
    @return: a 4x4 SE(3) matrix as a numpy array
    @note: Throws TypeError if we receive an incorrect type.
    """
    # if isinstance(msg, Pose):
    #     p, q = pose_to_pq(msg)
    # elif isinstance(msg, PoseStamped):
    #     p, q = pose_stamped_to_pq(msg)
    # elif isinstance(msg, Transform):
    #     p, q = transform_to_pq(msg)
    # elif isinstance(msg, TransformStamped):
    #     p, q = transform_stamped_to_pq(msg)
    # else:
    #     raise TypeError("Invalid type for conversion to SE(3)")
    p, q = transform_to_pq(msg)
    norm = np.linalg.norm(q)
    if np.abs(norm - 1.0) > 1e-3:
        raise ValueError(
            "Received un-normalized quaternion (q = {0:s} ||q|| = {1:3.6f})".format(
                str(q), np.linalg.norm(q)))
    elif np.abs(norm - 1.0) > 1e-6:
        q = q / norm
    g = tr.quaternion_matrix(q)
    g[0:3, -1] = p
    return g




def main():
    """Extract a folder of images from a rosbag.
    """
    rotpc = np.array([[1,0,0], [0,1,0], [0,0,-1]])
    args = {}
    bag_file = '/home/olorin/Desktop/IISc/ROS-ARM-Planning/rosbagfile.bag'
    depth_image_topic = '/camera/depth/image_raw'
    color_image_topic = '/camera/color/image_raw'
    tftopic = '/cameraposetransform'
    timetopic = '/clock'
    output_dir = 'tmp/'
    depthim = np.zeros((720,1280))
    transmatrix = np.eye(4,4)
    cam_intr = np.array([[347.997558594, 0.0, 320.0], [0.0, 347.997558594, 180.0], [0.0, 0.0, 1.0]])
    bag = rosbag.Bag(bag_file, "r")
    print(bag.get_start_time())
    print(bag.get_end_time())
    tf_t = tf.Transformer(True, rospy.Duration(360000.0))
    mychangeR = np.array([[0,-1,0], [0,0,1], [1,0,0]])
    # hjhg
    bridge = CvBridge()
    print("ASJH")
    count = 0
    allpcs = []

    for index, (topic, msg, t) in enumerate(bag.read_messages(topics=[color_image_topic,depth_image_topic, tftopic])):
        # print("ADHASGd")
        # print(topic, t)
        if(topic=='/cameraposetransform'):
            print(type(msg))
            # if(count==74):
            #     print(msg)
            #     print(transmatrix)
            
            # r = R.from_quat([msg.rotation.x, msg.rotation.y, msg.rotation.z, msg.rotation.w])
            # print(r.as_dcm())
            
            # transmatrix[:3, :3] = np.dot(mychangeR, r.as_dcm())
            # transmatrix[:3, :3] = r.as_dcm()
            # print(transmatrix)
            # transmatrix[:3, :3] =np.eye(3,3)
            # transmatrix[0,3] = msg.translation.x
            # transmatrix[1,3] = msg.translation.y
            # transmatrix[2,3] = msg.translation.z
            # print(transmatrix)/
            transmatrix = msg_to_se3(msg)

            # mbsst = r.as_rotvec()

        if(topic=='/camera/color/image_raw'):
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            # print(type(cv_img))
            # print(cv_img.shape)
            
            cv2.imwrite('/home/olorin/Desktop/depthimgs/imags/color-%06d.jpg'%(count), cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
            count+=1
        # if(topic=='/camera/depth/image_raw'):
        #     cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
        #     # print(type(cv_img))
        #     print(cv_img.shape)
        #     print(cv_img[0][0])
        #     #
        #     # np.save('/home/olorin/Desktop/depthimgs/depth-%06d.npy'%(count), cv_img)
        #     # np.save('/home/olorin/Desktop/depthimgs/pose-%06d.npy'%(count), transmatrix)
        #     # cv2.imwrite('/home/olorin/Desktop/depthimgs/depth-%06d.png'%(count), cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
        #     count+=1
        

        if(topic=='/camera/depth/image_raw'):
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
            np.save('/home/olorin/Desktop/depthimgs/imags/depth-%06d.npy'%(count), cv_img)
            np.savetxt('/home/olorin/Desktop/depthimgs/pose-%06d.txt'%(count), transmatrix)
            # print(cv_img[320][640])
            # print(transmatrix, count)
            # plt.imshow(cv_img)
            # plt.show()
            count+=1

            # cv2.imshow('IMAG', cv_img/1000 )
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

        #     cv_img = cv2.resize(cv_img, (640,360))
        #     md = np.max(cv_img)
        #     cv_img[cv_img>(md/5)]=0

            # np.save('/home/olorin/Desktop/depthimgs/%06d.npy'%(count), cv_img)
            
        #     if(count%5==0 and count>0):
        #         cv2.imshow('IMAG', cv_img/1000 )
        #         cv2.waitKey(0)
        #         cv2.destroyAllWindows()
        #         dept = cv2.rgbd.depthTo3d(cv_img/1000,cam_intr)
        #         # print(transmatrix)
        #         print(r.as_quat())
        #         r = R.from_dcm(transmatrix[:3, :3])
        #         # print(dept.shape)
        #         newdept = np.reshape(dept, (640*360,3))
        #         indicex = np.isnan(newdept).any(axis=1)
        #         pcpnts = newdept[indicex==False]
        #         print(pcpnts.shape)
        #         # print(transmatrix)
        #         # np.dot(transmatrix,pcpnts)
        #         pcpnts = r.apply(pcpnts)
        #         pcpnts = pcpnts+transmatrix[:3,3]
        #         # for pt in range(len(pcpnts)):
        #         #     if(pcpnts[pt][1]<0.17 and pcpnts[pt][1]>0.15):
        #         #         pcpnts[pt][2] = 0
        #         # pcpnts[pcpnts==0] = np.array([0,0,0])
        #         # print(newdept)
        #         # r2 = R.from_dcm(mychangeR)
        #         # print(newdept2)
        #         # newdept2 = newdept2-transmatrix[:3,3]
        #         # newdept2 = r2.apply(newdept2)
        #         # newdept2 = newdept[..., np.newaxis]
        #         point_cloud = o3d.geometry.PointCloud()
        #         point_cloud.points = o3d.utility.Vector3dVector(pcpnts)
        #         # print(transmatrix)
        #         point_cloud.rotate(rotpc)
        #         # print(np.asarray(point_cloud.points))
        #         # print(transmatrix[:3,:3])
        #         # point_cloud.rotate(transmatrix[:3,:3])
        #         # point_cloud.translate(transmatrix[:3,3])
        #         # point_cloud.transform(transmatrix)
        #         allpcs.append(point_cloud)
        #         o3d.visualization.draw_geometries(allpcs)

                
        #     # print(transmatrix)
        #     # print(count)
        #     # # print(mbsst)
        #     # # depthim = cv_img/1000
        #     # cv2.imshow('IMAG', cv_img/1000 )
        #     # cv2.waitKey(0)
        #     # cv2.destroyAllWindows()
        #     # # # print(cv_img)
        #     # dept = cv2.rgbd.depthTo3d(cv_img/1000,cam_intr)
            
        #     # newdept = np.reshape(dept, (720*1280,3))

        #     # indicex = np.isnan(newdept).any(axis=1)
        #     # pcpnts = newdept[indicex==False]
        #     # # pcpnts = 
        #     # # print(pcpnts)

        #     # point_cloud1 = o3d.geometry.PointCloud()
        #     # point_cloud1.points = o3d.utility.Vector3dVector(pcpnts)
        #     # # transmatrix[:3, :3] = np.linalg.inv(transmatrix[:3, :3])
        #     # # transmatrix[:3, 3] = -1*transmatrix[:3, 3]

        #     # # point_cloud.transform(transmatrix)
        #     # # print(dir(point_cloud))
        #     # # # kjg
        #     # # point_cloud1.rotate(rotpc)
        #     # # o3d.visualization.draw_geometries([point_cloud])


        #     # point_cloud = o3d.geometry.PointCloud()
        #     # point_cloud.points = o3d.utility.Vector3dVector(pcpnts)
        #     # transmatrix[:3, :3] = np.linalg.inv(transmatrix[:3, :3])
        #     # transmatrix[:3, 3] = -1*transmatrix[:3, 3]

        #     # point_cloud.transform(transmatrix)
        #     # # print(dir(point_cloud))
        #     # # # kjg
        #     # # point_cloud.rotate(rotpc)
        #     # o3d.visualization.draw_geometries([point_cloud1, point_cloud])

            

        #     count += 1

        # jhh
            # cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
            # cv2.imshow('IMAG', cv2.cvtColor(cv_img/1000,cv2.COLOR_BGR2RGB) )
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
        # print "Wrote image %i" % count
        # if(topic=='/tf'):
        #     
    print(count)
    bag.close()

    return

if __name__ == '__main__':
    main()
