##################################################
## Acceleration Configuration
##################################################
## Version: 2.2
## Email: info@vention.cc
## Status: tested
##################################################
import sys, os
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parentdir)
from _MachineMotion import *

enableDebug = True

# Define a callback to process controller gCode responses if desired. This is mostly used for debugging purposes.
def debug(data):
    if(enableDebug): print("Debug Message: " + data + "\n")

print ("Application Message: MachineMotion Program Starting \n")

mm = MachineMotion(debug, DEFAULT_IP_ADDRESS.usb_windows)
print ("Application Message: MachineMotion Controller Connected \n")

# Configure the axis number 1, 8 uSteps and 150 mm / turn for a timing belt
mm.configAxis(1, MICRO_STEPS.ustep_8, MECH_GAIN.timing_belt_150mm_turn)
print ("Application Message: MachineMotion Axis 1 Configured \n")

# Configuring the travel acceleration to 250 mm / second^2
mm.emitAcceleration(250)
print ("Application Message: Acceleration configured \n")

print ("Application Message: Program terminating ... \n")
time.sleep(1)
sys.exit(0)

