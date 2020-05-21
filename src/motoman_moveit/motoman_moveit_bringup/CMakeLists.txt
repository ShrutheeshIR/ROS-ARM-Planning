cmake_minimum_required(VERSION 2.8.3)
project(motoman_moveit_bringup)
find_package(catkin REQUIRED)
catkin_package()

####################################################
## !! Following code is supported only in indigo. ##
####################################################
# find_package(catkin REQUIRED COMPONENTS
#   roscpp
#   moveit_msgs
#   moveit_commander
#   moveit_core
#   moveit_ros_planning
#   moveit_ros_planning_interface
#   pluginlib
#   cmake_modules
#   )
# find_package(Boost REQUIRED system filesystem date_time thread)
# find_package(Eigen REQUIRED)
# catkin_package(
#   CATKIN_DEPENDS roscpp moveit_msgs
#   moveit_core
#   moveit_ros_planning_interface
#   )


###########
## Build ##
###########
########################################################
## !! Following CPP code is supported only in indigo. ##
########################################################
# include_directories(SYSTEM ${Boost_INCLUDE_DIR} ${EIGEN_INCLUDE_DIRS})
# include_directories(
#   include
#   ${catkin_INCLUDE_DIRS}
#   )
# include_directories(include ${catkin_INCLUDE_DIRS} ${Eigen_INCLUDE_DIRS})
# add_executable(move_group_plan_single_target
#   src/move_group_plan_single_target.cpp
#   )
# add_executable(move_groupe_plan_single_target_remove_octomap
#   src/move_group_plan_single_target_remove_octomap.cpp
#   )
# target_link_libraries(move_group_plan_single_target
#   ${catkin_LIBRARIES}
#   ${Boost_LIBRARIES}
#   ${EIGEN_LIBRARIES}
#   )
# target_link_libraries(move_groupe_plan_single_target_remove_octomap
#   ${catkin_LIBRARIES}
#   ${Boost_LIBRARIES}
#   ${EIGEN_LIBRARIES}
#   )
#############
## Install ##
#############
# Python scripts
set(PYTHON_SCRPTS
  scripts/moveit_command_sender_cartesian.py
  scripts/moveit_command_sender_multi.py
  scripts/moveit_command_sender.py
)
foreach(scripts ${PYTHON_SCRIPTS})
  catkin_install_python(PROGRAMS ${scripts}
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
endforeach(scripts)
# Install all files
set(CONFIG_DIRS
  config/motomini_with_gripper
  config/sda5
  config/sia5
  config/sia5_with_dhand
  config/sia5_with_dhand_and_multi_kinect
  config/sia5_with_kinectv2
  config/sia5_with_multi_kinectv2
  )
set(LAUNCH_DIRS
  launch/motomini
  launch/motomini/rviz
  launch/sda5
  launch/sda5/rviz
  launch/sia5
  launch/sia5/rviz
)
foreach(dir ${CONFIG_DIRS} ${LAUNCH_DIRS} scene)
  install(DIRECTORY ${dir}/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############
if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/motomini)
  roslaunch_add_file_check(launch/sda5)
  roslaunch_add_file_check(launch/sia5)
endif()
