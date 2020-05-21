cmake_minimum_required(VERSION 2.8.3)
project(motoman_moveit_config)
find_package(catkin REQUIRED)
catkin_package()

#############
## Install ##
#############
# Python scripts
set(PYTHON_SCRPTS
  scripts/moveit_joy.py
)
foreach(scripts ${PYTHON_SCRIPTS})
  catkin_install_python(PROGRAMS ${scripts}
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
endforeach(scripts)
# Install all files
foreach(dir launch)
  install(DIRECTORY ${dir}/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############
if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
  roslaunch_add_file_check(launch)
endif()
