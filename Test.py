from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *
import time


def main():
    # Get diameter from user
    while True:
        diameterInput = input("Enter the diameter of the phantom (in cm): ")
        try:
            diameter = float(diameterInput)
            if diameter <= 0:
                print("Diameter must be positive.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    #Get linear speed from user
    while True:
        speedInput = input("Enter the desired linear speed at the surface of the phantom (in cm/sec): ")
        try:
            linSpeed = float(speedInput)
            if(linSpeed < 0):
                print("Speed must be positive. ")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    #Convert linear speed to angular speed
    rad = diameter/2
    angSpeed = linSpeed / rad
    ROTATION_SPEED = angSpeed / (2*3.1415926535)

    #Initialize motor
    stepper1 = Stepper()
    stepper1.setChannel(1)
    stepper1.openWaitForAttachment(5000)
    stepper1.setTargetPosition(100000000)
    stepper1.setEngaged(True)

    #Set rescale factor to calibrate rotations per second
    stepper1.setRescaleFactor(0.0025)

    #Start motor
    velLimit = stepper1.setVelocityLimit(ROTATION_SPEED)
    velocityLimit = stepper1.getVelocityLimit()

    #Output set speed
    print("Rotational Speed: " + str(velocityLimit) + "revolutions/second")
    # currVel = stepper1.getVelocity()
    # print("Current Velocity: " + str(currVel))

    # Stop motor
    try:
        input("Press Enter to Stop\n")
    except (Exception, KeyboardInterrupt):
        pass

    #Close motor channel    
    stepper1.close()


main()
