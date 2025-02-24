from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *
import time


def main():
    #Enter desired rotation speed in RPS
    ROTATION_SPEED = 0
    userInput = input("Enter desired rotation speed (revolutions per second): ")
    try:
        ROTATION_SPEED = float(userInput)
    except:
        print("Invalid input. Please enter an integer.")
        
    stepper1 = Stepper()
    stepper1.setChannel(1)
    
    stepper1.openWaitForAttachment(5000)

    
    stepper1.setTargetPosition(10000000)
    stepper1.setEngaged(True)

    
    currVel = stepper1.getVelocity()
    stepper1.setRescaleFactor(0.0025)
    velLimit = stepper1.setVelocityLimit(ROTATION_SPEED)
    velocityLimit = stepper1.getVelocityLimit()
    print("Current Velocity: " + str(currVel))
    print("Velocity Limit: " + str(velocityLimit))


    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass


    stepper1.close()


main()
