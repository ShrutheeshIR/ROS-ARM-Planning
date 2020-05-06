# Install script for directory: /home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_robot/motoman_description/catkin_generated/installspace/motoman_description.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/cmake" TYPE FILE FILES
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_robot/motoman_description/catkin_generated/installspace/motoman_descriptionConfig.cmake"
    "/home/olorin/Desktop/IISc/ROS-ARM-Planning/build/motoman_robot/motoman_description/catkin_generated/installspace/motoman_descriptionConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description" TYPE FILE FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/launch/motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/launch/motomini/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/launch/motomini/rviz" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/launch/motomini/rviz/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/meshes/motomini/collision" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/meshes/motomini/collision/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/meshes/motomini/visual" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/meshes/motomini/visual/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/meshes/sensor/visual/COLLADA" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/meshes/sensor/visual/COLLADA/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/meshes/tool" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/meshes/tool/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/robots/motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/robots/motomini/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/urdf" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/urdf/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/urdf/motomini" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/urdf/motomini/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/urdf/sensor" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/urdf/sensor/")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/motoman_description/urdf/tool" TYPE DIRECTORY FILES "/home/olorin/Desktop/IISc/ROS-ARM-Planning/src/motoman_robot/motoman_description/urdf/tool/")
endif()

