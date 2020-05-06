cmake_minimum_required(VERSION 2.8.3)
project(motoman_description)
find_package(catkin REQUIRED)
catkin_package()

###########
# Install #
###########
set(LAUNCH_DIRS
  launch/motomini
  launch/motomini/rviz

)
set(MESH_DIRS
  meshes/motomini/collision
  meshes/motomini/visual
  meshes/sensor/visual/COLLADA
  meshes/tool
)
set(URDF_DIRS
  robots/motomini
  urdf
  urdf/motomini
  urdf/sensor
  urdf/tool
)

foreach(dir ${LAUNCH_DIRS} ${MESH_DIRS} ${URDF_DIRS})
  install(DIRECTORY ${dir}/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

########
# Test #
########
if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch/motomini)
endif()

