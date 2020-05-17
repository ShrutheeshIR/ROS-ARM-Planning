# Install script for directory: /home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_config_motomini

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_config_motomini/catkin_generated/installspace/motoman_moveit_config_motomini.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_config_motomini/cmake" TYPE FILE FILES
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_config_motomini/catkin_generated/installspace/motoman_moveit_config_motominiConfig.cmake"
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_moveit/motoman_moveit_config_motomini/catkin_generated/installspace/motoman_moveit_config_motominiConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_config_motomini" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_config_motomini/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_config_motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_config_motomini/launch" REGEX "/setup\\_assistant\\.launch$" EXCLUDE)
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_moveit_config_motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_moveit/motoman_moveit_config_motomini/config")
endif()

