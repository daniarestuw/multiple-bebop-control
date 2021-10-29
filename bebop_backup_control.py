# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys
import termios
import tty
import time


from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist




def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def stop():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.0
	tw.linear.z = 0.0

	control_pub.publish(tw)

def takeoff():
	takeoff_pub.publish(Empty())

def land():
	land_pub.publish(Empty())

def forward():
	tw = Twist()
	tw.linear.x = 0.3#0.3
	tw.linear.y = 0.0
	tw.linear.z = 0.0

	control_pub.publish(tw)
	

def back():
	tw = Twist()
	tw.linear.x = -0.3
	tw.linear.y = 0.0
	tw.linear.z = 0.0

	control_pub.publish(tw)

	
def left():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.3
	tw.linear.z = 0.0

	control_pub.publish(tw)
	
def right():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = -0.3
	tw.linear.z = 0.0

	control_pub.publish(tw)
	

def right_2():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.0
	tw.linear.z = 0.0
	tw.angular.z = -0.3

	control_pub.publish(tw)

def left_2():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.0
	tw.linear.z = 0.0
	tw.angular.z = 0.3

	control_pub.publish(tw)

def up():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.0
	tw.linear.z = 0.3

	control_pub.publish(tw)
	

def down():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.0
	tw.linear.z = -0.3

	control_pub.publish(tw)
	

def menu():
	print("o: takeoff")
	print("l: land")
	print("w: foward")
	print("a: left")
	print("s: back")
	print("x: back")
	print("q: left_2")
	print("e: right_2")
	print("j: up")
	print("k: down")

if __name__ == '__main__':
	x = 0
	y = 0
	z = 0

	rospy.init_node('example_node', anonymous=True)
	takeoff_pub = rospy.Publisher("bebop/takeoff", Empty, queue_size=10)
	land_pub = rospy.Publisher("bebop/land", Empty, queue_size=10)

	control_pub = rospy.Publisher("bebop/cmd_vel", Twist, queue_size=10)

	menu()

	while True:
                #soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                #soc.bind((host, port))
                
                #data, addr = soc.recvfrom(1024)

                #print "IP: ", addr
                #print "Data: ", data
                #if data == 'A':
                #    print "ABC"
                #else:
                #    print "", data

                
		char = getch()
		#char = data
		#soc.close()
		
		if (char == "w"):
			print("forward")
			forward()

		elif (char == "a"):
			print("left")
			left()
	
		elif (char == "s"):
			print("backward")
			back()
		elif (char == "d"):
			print("right")
			right()
		elif (char == "j"):
			print("up")
			up()
	
		elif (char == "k"):
			print("down")
			down()
	
		elif (char == "q"):
			print("left yaw")
			left_2()
	
		elif (char == "e"):
			print("right yaw")
			right_2()
	
		elif (char == "o"):
			print("takeoff")
			takeoff()
			
		elif (char == "l"):
			print("land")
			land()
		elif (char == "x"):
			print("land")
			land()



		else:
			break
