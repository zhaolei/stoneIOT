#!/usr/bin/env python

from __future__ import print_function

from xnode.srv import rq,rqResponse
import rospy

def handle_add_two_ints(req):
    print("Returning [%s + %s = %s]"%(req.A, req.B, (req.A + req.B)))
    return rqResponse(req.A + req.B)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('rq', rq, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
