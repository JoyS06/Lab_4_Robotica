"""
Allows to use the service dynamixel_command 
"""
from cmath import pi
import rospy
import time
from std_msgs.msg import String
from dynamixel_workbench_msgs.srv import DynamixelCommand
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import numpy as np

def joint_publisher():
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1"]
        point = JointTrajectoryPoint()
        point.positions = [0, 0, 0, 0, 0]    
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

def callback(data):
    global PosActual
    PosActual=np.multiply(data.position,180/pi)

    
def listener():
    rospy.init_node('joint_listener', anonymous=True)
    rospy.Subscriber("/dynamixel_workbench/joint_states", JointState, callback)
    #rospy.spin()

def jointCommand(command, id_num, addr_name, value, time):
    #rospy.init_node('joint_node', anonymous=False)
    rospy.wait_for_service('dynamixel_workbench/dynamixel_command')
    try:        
        dynamixel_command = rospy.ServiceProxy('/dynamixel_workbench/dynamixel_command', DynamixelCommand)
        result = dynamixel_command(command,id_num,addr_name,value)
        rospy.sleep(time)
        return result.comm_result
    except rospy.ServiceException as exc:
        print(str(exc))

if __name__ == '__main__':
    try:
        listener()#activa listener

        
        PosHome=[514,510,818,512,512]
        pos1An=[597,597,888,444,512]
        pos2An=[393,630,716,616,512]
        pos3An=[802,445,1000,599,512]
        pos4An=[786,395,1000,360,546]

        #posicion en grados
        posHomeDegree=[0,0,0,0,0]
        pos1Degree=[25,25,20,-20,0] 
        pos2Degree=[-35,35,-30,30,0]
        pos3Degree=[85,-20,55,25,0] 
        pos4Degree=[80,-35,55,-45,0]

        ListaPosiciones = [PosHome,pos1An,pos2An,pos3An,pos4An]
        ListaPosicionesDegree = [posHomeDegree,pos1Degree,pos2Degree,pos3Degree,pos4Degree]
        print(" ")
        print("Angulos:")
        print("Posicion 1: [0,0,0,0,0] ")
        print("Posicion 2: [25,25,20,-20,0] ")
        print("Posicion 3: [-35,35,-30,30,0] ")
        print("Posicion 4: [85,-20,55,25,0] ")
        print("Posicion 5: [80,-35,55,-45,0] ")
        while True:
            print(" ")
            numPosicion= int(input("Elija posicion: "))

            posiElegida=ListaPosiciones[numPosicion-1]
            posiElegidaDegree=ListaPosicionesDegree[numPosicion-1]

            for i in range(5):
                jointCommand('', i+1,'Torque_Limit', 400, 0)
                jointCommand('', i+1, 'Goal_Position', posiElegida[i] ,0.5)


            print(" ")
            print("Valores actuales de las Articulación  en grados: ")
            for i  in range(5):
                print("Articulación "+str(i)+" = "+str("{0:.2f}".format(PosActual[i]))+ " Error :"+str("{0:.2f}".format(abs(PosActual[i]-posiElegidaDegree[i]))))
            print(" ")
    
                
        # Goal_Position (0,1023)
        # Torque_Limit (0,1023)

        #time.sleep(0.5)
    except rospy.ROSInterruptException:
        pass