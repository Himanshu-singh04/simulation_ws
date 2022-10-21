#!/usr/bin/env python4
from cmath import acos, atan
import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import JointState
class armnodeclass:

    def __init__(self):
        # axes[0] -> no map
        # axes[1] -> move in +-y 1/-1
        # axes[2] -> no map
        # axes[3] -> move in -+x 1/-1
        # buttons[1] -> circle +z 1/0
        # buttons[3] -> square -z 1/0
        rospy.init_node('arm_teleop_node')
        self.x=0 #initialize according to arm
        self.y=582.59 #initialize according to arm in mm
        self.z=-91.62 #initialize according to arm in mm
        self.p=440 #initialize according to length of shoulder
        self.q=375 #initialize according to length of arm
        self.a=(atan(self.x/self.y)).real                                   #base servo angle
        self.l=(self.x**2 +self.y**2)**0.5
        self.b=(atan(self.z/self.l)).real
        self.t=(acos((self.p**2+self.l**2-self.q**2)/(2*self.p*self.l))).real
        self.s=self.t+self.b                                                #shoulder angle
        self.k=(acos((self.p**2+self.q**2-self.l**2)/(2*self.p*self.q))).real      #arm angle
        # self.rate=rospy.Rate(10)
        self.joint_angles=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        # initialize all initial params of arm
        self.pub_joint_states=rospy.Publisher('joint_states',JointState,queue_size=10)
        self.sub_joy=rospy.Subscriber('joy',Joy,callback=self.updatePos)
        # initialize ar lengths and rest state angles
        # figure out rough 
        # joint_states 
        # establish upper limits of the arm
        # 90, 30.5, 92.36, 
        rospy.spin()

    def updatePos(self,data):
        
        if (data.axes[1]<-0.5):
            self.y-=1 #decide factor by which it has to be reduced
        elif (data.axes[1]>0.5):
            self.y+=1
        if (data.axes[3]<-0.5):
            self.x+=1
        elif (data.axes[3]>0.5):
            self.x-=1
        if (data.buttons[1]==1): #map for +z):
            self.z+=1
        elif(data.buttons[3]==1): #map for -z:
            self.z-=1
        # call moveToPos() to compute joint angles 
        self.moveToPos()
        print("This is the joy subscriber. figure out increment/decrement acc to joy value")

    def moveToPos(self):
        # figure out joint angles
        self.a=(atan(self.x/self.y)).real
        self.l=(self.x**2 +self.y**2)**0.5
        self.b=(atan(self.z/self.l)).real
        self.t=(acos((self.p**2+self.l**2-self.q**2)/(2*self.p*self.l))).real
        self.s=self.t+self.b
        self.k=(acos((self.p**2+self.q**2-self.l**2)/(2*self.p*self.q))).real
        # call moveToAngle to publish joint angles to micrcontroller
        self.moveToAngle()
        print("joint angles have been figured out")

    def moveToAngle(self):
        # publish joint angles to microcontroller 
        # the microcontroller must figure out a way to remember prev states and go to new published states
        joint_message=JointState()
        joint_names=["arm_joint_1","arm_joint_2","arm_joint_3","arm_joint_4","arm_joint_5","arm_joint_6","arm_joint_7","arm_joint_8"]
        joint_message.name=joint_names
        self.joint_angles[0]=self.a
        self.joint_angles[1]=self.s
        self.joint_angles[2]=self.k
        joint_message.position=self.joint_angles
        self.pub_joint_states.publish(joint_message)        

if __name__ == '__main__':
    ob=armnodeclass()
