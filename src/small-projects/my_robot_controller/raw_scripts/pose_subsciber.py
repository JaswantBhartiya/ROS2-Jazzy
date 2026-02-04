#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class MyNode(Node):

	def __init__(self):
		super().__init__("pose_subscriber")
		self.pose_sub = self.create_subscription(Pose, "/turtle1/pose", pose_callback, 10)

	def pose_callback(self, pose:Pose):
		self.get_logger().info(str(pose))

def main(args=None):
	rclpy.init(args=args)
	node = MyNode()
	rclpy.spin(node)
	rclpy.shutdown()
