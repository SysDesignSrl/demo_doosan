#!/usr/bin/env python
import os
import sys
sys.dont_write_bytecode = True
sys.path.append(os.path.abspath(os.path.join('/home/nicola/ros/doosan_ws/src/common/imp')))     # get import path : DSR_ROBOT.py

# ROS
import rospy
import std_msgs.msg
import std_srvs.srv

# Doosan Robotics library
ROBOT_ID    = "dsr01"
ROBOT_MODEL = "m1013"
import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *


def on_shutdown():
    # stop(DR_QSTOP)
    pass


if __name__ == '__main__':

    rospy.init_node('jog_teleop')
    rospy.on_shutdown(on_shutdown)

    set_robot_mode(ROBOT_MODE_MANUAL)   # jog is only available in manual mode.

    pos1 = posx(100, 0, 0, 0, 0, 0)
    pos2 = posx(0, 100, 0, 0, 0, 0)

    count = 0
    rate = rospy.Rate(0.1)                # 0.1Hz
    while not rospy.is_shutdown():

        if count % 2 == 0:
            pos = pos1
        else:
            pos = pos2

        err = movec(pos1, pos2, time=10, ref=DR_TOOL)
        if err != 0:
            rospy.logerr("Error: %d", err)

        count += 1
        rate.sleep()
