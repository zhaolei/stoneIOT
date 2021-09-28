#!/usr/bin/env python
# license removed for brevity
#import sys
#sys.path.append('/home/stone/ros/devel/lib/python2.7/dist-packages/')
#import site
#site.addsitedir('/home/stone/devel/lib/python2.7/dist-packages/')

import rospy
from std_msgs.msg import String
from xnode.msg import Num 

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    pubx = rospy.Publisher('debug_node', Num, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(1) # 10hz

    xnum = Num(2, "debug")
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        
        xnum.name = hello_str
        pubx.publish(xnum)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
