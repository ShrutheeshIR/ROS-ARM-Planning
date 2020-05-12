# ROS-ARM-Planning
Gazebo ROS based ARM Simulator using Intel RealSense

Command : roslaunch motoman_gazebo motomini_with_table_parts.launch
Command to move the robot mount : 
1. rostopic pub -1 /mountbodcontroller/command std_msgs/Float64 "data: 0.3" (for vertical mount)
2. rostopic pub -1 /mountcameraledgecontroller/command std_msgs/Float64 "data: -0.4" (for the tiny ledge that the camera is attached on)
