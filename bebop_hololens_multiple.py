# -*- coding: utf-8 -*-
#!/usr/bin/env python

import rospy
import sys
import termios
import tty
import time
import socket


from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


host = "192.168.21.100"
port = 1234


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

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


def menu():
	print("o: takeoff")
	print("l: land")
	print("w: forward")
	print("a: left")
	print("d: right")
    print("s: back")
    print("n: takeoff 2nd bebop")
	print("m: land 2nd bebop")
	print("y: forward 2nd bebop")
	print("g: left 2nd bebop")
    print("j: right 2nd bebop")
	print("h: back 2nd bebop")

#2nd Bebop
    
def takeoff2():
	takeoff_pub.publish(Empty())

def land2():
	land_pub.publish(Empty())

def forward2():
	tw = Twist()
	tw.linear.x = 0.3#0.3
	tw.linear.y = 0.0
	tw.linear.z = 0.0

	control_pub.publish(tw)

def back2():
	tw = Twist()
	tw.linear.x = -0.3
	tw.linear.y = 0.0
	tw.linear.z = 0.0

	control_pub.publish(tw)

def left2():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = 0.3
	tw.linear.z = 0.0

	control_pub.publish(tw)

def right2():
	tw = Twist()
	tw.linear.x = 0.0
	tw.linear.y = -0.3
	tw.linear.z = 0.0

	control_pub.publish(tw)


def menu2():

    
    


if __name__ == '__main__':
	x = 0
	y = 0
	z = 0

	rospy.init_node('example_node', anonymous=True)
	takeoff_pub = rospy.Publisher("bebop/takeoff", Empty, queue_size=10)
	land_pub = rospy.Publisher("bebop/land", Empty, queue_size=10)

	control_pub = rospy.Publisher("bebop/cmd_vel", Twist, queue_size=10)

	menu()
    menu2()

	while True:
                soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                soc.bind((host, port))
                
                data, addr = soc.recvfrom(1024)

                #print "IP: ", addr
                print "Data: ", data
                if data == 'A':
                    print "ABC"
                else:
                    print "", data

                
		#char = getch()
		char = data
		soc.close()

		if (char == "w"):
			print("forward")
			forward()
            
        elif (char == "s"):
			print("backward")
			back()
	
		elif (char == "a"):
			print("left")
			left()
            
		elif (char == "d"):
			print("right")
			right()

		elif (char == "o"):
			print("takeoff")
			takeoff()
			
		elif (char == "l"):
			print("land")
			land()
        
#2nd BEBOP
        
        elif (char == "y"):
			print("forward")
			forward2()
            
        elif (char == "h"):
			print("backward")
			back2()
            
        elif (char == "g"):
			print("left")
			left2()
	
		elif (char == "j"):
			print("right")
			right2()
            
		elif (char == "n"):
			print("takeoff")
			takeoff2()
			
		elif (char == "m"):
			print("land")
			land2()

		else:
			break
