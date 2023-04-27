# Dynamixel_Python_OSC
python script allowing communication between OSC and Dynamixel servo motor

This Python script can run from the commannd line (Terminal, Power Shell, Cmd...)
Playing in background, it allows to use OSC commands to move the servo and retrieve the position.

To use it, you need:
- working Dynamixel servo, I tested it with the XL430-W250-T model. With other models you may have to change the "connect" line
- Dynamixel U2D2 interface allowing serial communication via USB
- DC alimentation for the motor
- Python installed on your computer
- Command Line Interface

Install python-osc module
$ pip install python-osc
Install dynamixel python library (a simplified one)
$ pip install dynamixel-controller

With Dynamixel-Wizard application, adjust the motor settings:
- motor ID (1 in the actual script)
- baud rate (57600 bps in the actual script)
- RDT (20 microsec in actual script)
- mode to Extended Position Control
- protocol (2.0 in actual script)

In the python script, adjust your settings:
- OSC out IP address and port
- OSC in port
- serial port
- motor ID
- motor protocol
Save it

cd to the folder containing the python script
run the script in Python
$ python pythonDynamixelOSC.py

With any app sending/receiving OSC (TouchDesigner, Isadora, Max/Msp, PureData...)
with all values as integer
- change the velocity OSC address '/speed' (step/second)
- change the acceleration OSC address '/accel' (step/second/second)
- move to position OSC address '/goal' (step, alway positive)
- retrieve position OSC address '/go' (any value, you will receive the position on OSC address '/position')

My motor have 4096 step / rotation

I give an example in TouchDesigner allowing to move the motor and receive the position during the move
