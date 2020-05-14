
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


def main():
    """Extract a folder of images from a rosbag.
    """
    rotpc = np.array([[1,0,0], [0,-1,0], [0,0,-1]])
    args = {}
    bag_file = '/home/olorin/Desktop/IISc/ROS-ARM-Planning/2020-05-13-20-22-51.bag'
    depth_image_topic = '/camera/depth/image_raw'
    color_image_topic = '/camera/color/image_raw'
    tftopic = '/cameraposetransform'
    timetopic = '/clock'
    output_dir = 'tmp/'
    depthim = np.zeros((720,1280))
    transmatrix = np.eye(4,4)
    cam_intr = np.array([[695.9951171875, 0.0, 640.0], [0.0, 695.9951171875, 360.0], [0.0, 0.0, 1.0]])
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
            # print(msg)
            r = R.from_quat([msg.rotation.x, msg.rotation.y, msg.rotation.z, msg.rotation.w])
            # print(r.as_dcm())
            
            # transmatrix[:3, :3] = np.dot(mychangeR, r.as_dcm())
            transmatrix[:3, :3] = r.as_dcm()
            # print(transmatrix)
            # transmatrix[:3, :3] =np.eye(3,3)
            transmatrix[0,3] = msg.translation.x
            transmatrix[1,3] = msg.translation.y
            transmatrix[2,3] = msg.translation.z
            # print(transmatrix)
            mbsst = r.as_rotvec()

        if(topic=='/camera/color/image_raw'):
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            print(type(cv_img))
            print(cv_img.shape)
            
            cv2.imwrite('/home/olorin/Desktop/depthimgs/color-%06d.jpg'%(count), cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
            count+=1
        if(topic=='/camera/depth/image_raw'):
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
            print(type(cv_img))
            print(cv_img.shape)
            np.save('/home/olorin/Desktop/depthimgs/depth-%06d.npy'%(count), cv_img)
            # cv2.imwrite('/home/olorin/Desktop/depthimgs/depth-%06d.png'%(count), cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
            count+=1

        # if(topic=='/camera/depth/image_raw'):
        #     cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough").astype(np.float32)
        #     md = np.max(cv_img)
        #     cv_img[cv_img>(md/5)]=0

        #     np.save('/home/olorin/Desktop/depthimgs/%06d.npy'%(count), cv_img)
        #     np.savetxt('/home/olorin/Desktop/depthimgs/%06d.txt'%(count), transmatrix)
        #     if(count%10==0 and count>75):
        #         cv2.imshow('IMAG', cv_img/1000 )
        #         cv2.waitKey(0)
        #         cv2.destroyAllWindows()
        #         dept = cv2.rgbd.depthTo3d(cv_img/1000,cam_intr)
        #         # print(transmatrix)
        #         print(r.as_euler('xyz'))
        #         r = R.from_dcm(np.linalg.inv(transmatrix[:3, :3]))
        #         # print(dept.shape)
        #         newdept = np.reshape(dept, (720*1280,3))
        #         indicex = np.isnan(newdept).any(axis=1)
        #         pcpnts = newdept[indicex==False]
        #         # print(newdept)
        #         r2 = R.from_dcm(mychangeR)
        #         newdept2 = r.apply(pcpnts)
        #         # print(newdept2)
        #         newdept2 = newdept2-transmatrix[:3,3]
        #         # newdept2 = r2.apply(newdept2)
        #         # newdept2 = newdept[..., np.newaxis]
        #         point_cloud = o3d.geometry.PointCloud()
        #         point_cloud.points = o3d.utility.Vector3dVector(newdept2)
        #         # print(transmatrix)
        #         point_cloud.rotate(rotpc)
        #         # print(np.asarray(point_cloud.points))
        #         # print(transmatrix[:3,:3])
        #         # point_cloud.rotate(transmatrix[:3,:3])
        #         # point_cloud.translate(transmatrix[:3,3])
        #         # point_cloud.transform(transmatrix)
        #         allpcs.append(point_cloud)
        #         # o3d.visualization.draw_geometries(allpcs)

                
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
