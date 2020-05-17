# Install script for directory: /home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/olorin/Desktop/IISc/ROS-ARM-Planning/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_bringup/catkin_generated/installspace/motoman_moveit_bringup.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/cmake" TYPE FILE FILES
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_bringup/catkin_generated/installspace/motoman_moveit_bringupConfig.cmake"
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_bringup/catkin_generated/installspace/motoman_moveit_bringupConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/motomini_with_gripper" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/motomini_with_gripper/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sda5" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sda5/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sia5" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sia5/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sia5_with_dhand" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sia5_with_dhand/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sia5_with_dhand_and_multi_kinect" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sia5_with_dhand_and_multi_kinect/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sia5_with_kinectv2" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sia5_with_kinectv2/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/config/sia5_with_multi_kinectv2" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/config/sia5_with_multi_kinectv2/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/motomini/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/motomini/rviz" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/motomini/rviz/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/sda5" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/sda5/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/sda5/rviz" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/sda5/rviz/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/sia5" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/sia5/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/launch/sia5/rviz" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/launch/sia5/rviz/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_bringup/scene" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_bringup/scene/")
endif()

