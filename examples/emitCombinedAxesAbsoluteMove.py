from _MachineMotion import *

#Declare parameters for combined absolute move
speed = 500
acceleration = 500
axesToMove = [1,2,3]
positions = dict(zip(axesToMove, [50, 100, 50]))
mechGain = MECH_GAIN.timing_belt_150mm_turn

#Load parameters for combined absolute move
mm = MachineMotion(DEFAULT_IP_ADDRESS.usb_windows)
mm.emitSpeed(speed)
mm.emitAcceleration(acceleration)
for axis in axesToMove:
    mm.configAxis(axis, MICRO_STEPS.ustep_8, mechGain)
print("All Axes Moving Home Sequentially")
mm.emitHomeAll()
mm.waitForMotionCompletion()
print("All Axes homed.")

# Simultaneously moves three axis:
#   Moves axis 1 to absolute position 50
#   Moves axis 2 to absolute position 100
#   Moves axis 3 to absolute position 50
mm.emitCombinedAxesAbsoluteMove(axesToMove, positions)
mm.waitForMotionCompletion()
for axis in axesToMove:
    print("Axis " + str(axis) + "moved to position " + str(positions[axis]))



