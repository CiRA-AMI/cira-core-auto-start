import os
from subprocess import Popen
import subprocess
import time

print('###########  CiRA Autorun ############')
import getpass
username = getpass.getuser()
print('user : ', username)

# CiRA CORE Parameter
FLOW_FILE = ""                  # .flow or .npj file path for example : "/home/cira/cira_ai.flow"
HIDE_TOOLBAR = "true"           # set "true" to "false"
LOCK_CIRA_CORE = "false"        # set "true" to "false" : lock/unlock by control+L and type password
SHOW_FULLSCREEN = "true"        # set "true" to "false" : exit by control+F

# CiRA Arduino IO Parameter
USER_PASS = ""                  # password of your user
RUN_ARDUINO = False

time.sleep(10)

def find_ros_version():
    preferred_versions = ['noetic', 'melodic']
    ros_base_path = '/opt/ros/'
    for version in preferred_versions:
        version_path = os.path.join(ros_base_path, version)
        if os.path.isdir(version_path):
            return version  # Return the first found version
    return None

ros_version = find_ros_version()
if ros_version:
    print(f'ROS version found: {ros_version}')
else:
    print('No preferred ROS version found in /opt/ros/')


# 1 run ros core
cmd = f"source ~/.bashrc && source /opt/ros/{ros_version}/setup.bash && roscore"
print("cmd : ", cmd)
Popen(["gnome-terminal", '--' , 'bash', '-c' , cmd])
time.sleep(3)

# 3 run cira core
cmd = "source ~/.bashrc && LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib && "
cmd = cmd + f"source /opt/ros/{ros_version}/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && "
cmd = cmd + f"while true; do rosrun cira_core cira_core_run  _file:=\'{FLOW_FILE}\' _hide_toolbar:={HIDE_TOOLBAR} _lock:={LOCK_CIRA_CORE} _fullscreen:={SHOW_FULLSCREEN}; sleep 1s; done ;$SHELL"
print("cmd : ", cmd)
Popen(["gnome-terminal", '--' , 'bash', '-c' , cmd])
time.sleep(2)

###############

if RUN_ARDUINO :
    # 2 run arduino
    cmd = "source ~/.bashrc && LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/usr/local/lib && export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:/opt/qt511/lib && "
    cmd = cmd + f"source /opt/ros/{ros_version}/setup.bash && source ~/.cira_core_install/cira_libs_ws/install/setup.bash --extend && while true; do rosrun cira_arduino_io cira_arduino_io_run _pass:={USER_PASS}; sleep 1s; done ;$SHELL"
    print("cmd : ", cmd)
    Popen(["gnome-terminal", '--' , '/bin/bash', '-c' , cmd])
    time.sleep(2)
