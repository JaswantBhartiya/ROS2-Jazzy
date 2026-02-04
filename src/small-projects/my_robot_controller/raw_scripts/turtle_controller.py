#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class MyNode(Node):
	
	def __init__(self):
		super().__init__("turtle_controller")
		self.pose_sub =  self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
		self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
		self.get_logger().info("Node has been started.")

	def pose_callback(self, pose:Pose):
		cmd = Twist()		
		if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
			cmd.linear.x = 1.0
			cmd.angular.z = 0.9
		else:
			cmd.linear.x = 5.0
			cmd.angular.z = 0.0
		self.cmd_vel_pub.publish(cmd)			

def main(args=None):
	rclpy.init(args=args)
	node = MyNode()
	rclpy.spin(node)
	rclpy.shutdown()