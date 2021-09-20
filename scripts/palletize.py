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

    rospy.init_node('palletize')
    rospy.on_shutdown(on_shutdown)

    # set autonomous robot mode
    err = set_robot_mode(ROBOT_MODE_AUTONOMOUS)
    if err != 0:
        rospy.logerr("Error: %d", err)

    # program
    for i in range(5):

        for j in range(2):

            # define positions
            posx_prepick  = posx(         0, 500,       500,  0, 180, 0)
            posx_pick     = posx(         0, 500,         0,  0, 180, 0)
            posx_preplace = posx(-100*j-500,   0,       500, 90, 180, 0)
            posx_place    = posx(-100*j-500,   0, 100*i-500, 90, 180, 0)

            # go to pre-pick
            err = movejx(posx_prepick, time=5.0, sol=2)
            if err != 0:
                rospy.logerr("Error: %d", err)

            # pick
            err = movel(posx_pick, time=5.0)
            if err != 0:
                rospy.logerr("Error: %d", err)

            err = movel(posx_prepick, time=5.0)
            if err != 0:
                rospy.logerr("Error: %d", err)

            # go to pre-place
            err = movejx(posx_preplace, time=5.0, sol=2)
            if err != 0:
                rospy.logerr("Error: %d", err)

            # place
            err = movel(posx_place, time=5.0)
            if err != 0:
                rospy.logerr("Error: %d", err)

            err = movel(posx_preplace, time=5.0)
            if err != 0:
                rospy.logerr("Error: %d", err)
