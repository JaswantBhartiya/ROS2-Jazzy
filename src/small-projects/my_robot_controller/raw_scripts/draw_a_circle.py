#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyNode(Node):

	def __init__(self):
		super().__init__("draw_circle")
		self.cmd_vel_pub = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
		self.timer = self.create_timer(0.5, self.draw_circle)
		self.get_logger().info("Node has been started.")

	def draw_circle(self):
		cmd = Twist()
		cmd.linear.x = 2.0
		cmd.angular.z = 1.0
		self.cmd_vel_pub.publish(cmd)

def main(args=None):
	rclpy.init(args=args)
	node = MyNode()
	rclpy.spin(node)
	rclpy.shutdown()
