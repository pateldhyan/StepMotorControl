from Phidget22.Phidget import *
from Phidget22.Devices.Stepper import *
import time

#Declare any event handlers here. These will be called every time the associated event occurs.

def main():
	#Enter desired rotation speed in RPS
	ROTATION_SPEED = 1

	#Create your Phidget channels
	stepper1 = Stepper()

	#Set addressing parameters to specify which channel to open (if any)
	stepper1.setChannel(1)
	

	#Assign any event handlers you need before calling open so that no events are missed.

	#Open your Phidgets and wait for attachment
	stepper1.openWaitForAttachment(5000)

	#Do stuff with your Phidgets here or in your event handlers.
	stepper1.setTargetPosition(10000)
	stepper1.setEngaged(True)
	
	stepper1.setRescaleFactor(0.0075)
	currVel	= stepper1.getVelocity()
	velLimit = stepper1.setVelocityLimit(ROTATION_SPEED)
	velocityLimit = stepper1.getVelocityLimit()
	print("Current Velocity: " + str(currVel))
	print("Velocity Limit: " + str(velocityLimit))

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	#Close your Phidgets once the program is done.
	stepper1.close()

main()
