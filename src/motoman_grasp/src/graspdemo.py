import sys
import rospy
import moveit_commander
import geometry_msgs.msg
import numpy as np
from scipy.spatial.transform import Rotation as R

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('moveitcommander', anonymous=True)
robot = moveit_commander.RobotCommander()
mountgroup = moveit_commander.MoveGroupCommander('Mount')
mountgroup.set_joint_value_target([-0.1, 0.4])
mountgroup.go()



# hand_group = moveit_commander.MoveGroupCommander('Hand')
# poss = np.load('/home/olorin/Desktop/IISc/pose.npy')
# r = R.from_dcm(poss[:3,:3]).as_quat()
# print(poss)
# print(R.from_dcm(poss[:3,:3]).as_euler('xyz'))
# hand_group.set_joint_value_target([0.015, 0.015])
# plan2 = hand_group.go()


# arm_group = moveit_commander.MoveGroupCommander('Arm')
# arm_group.set_planning_time(10)
# pose_target = geometry_msgs.msg.Pose()
# # # pose_target.orientation.w = r[3]
# # # pose_target.orientation.x = r[0]
# # # pose_target.orientation.y = r[1]
# # # pose_target.orientation.z = r[2]
# pose_target.position.x = 0.20
# pose_target.position.y = 0
# pose_target.position.z = 0.20
# # arm_group.set_pose_target(pose_target)
# # # arm_group.set_named_target('DefaultArm')
# plan1 = arm_group.go(wait=True)

# # hand_group.set_joint_value_target([0.0125, 0.00125])
# # hand_group.stop

# # hand_group.set_named_target('Close')
# # print(hand_group.get_current_pose('gripper_finger_link_l'))
# # plan3 = hand_group.go()

rospy.sleep(5)
moveit_commander.roscpp_shutdown()

