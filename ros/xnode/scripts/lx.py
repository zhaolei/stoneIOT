#!/usr/bin/env python

import rospy
import json
from std_msgs.msg import String
from xnode.msg import Num 

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def callbackx(data):
    rospy.loginfo(rospy.get_caller_id() + ': %d , %s', data.num, data.name)
    
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("chatter", String, callback)
    rospy.Subscriber("debug_node", Num, callbackx)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
