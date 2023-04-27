# pip install dynamixel-controller
# pip install python-osc
# use Dynamixel Wizard to set XL430-W250 motor:
# ID, Baud Rate (57600 bps), RDT (20 microsec), Extended Position control
# Protocol 2.0 
from dynio import *
from pythonosc import udp_client
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
# initialize position
goal = 0
accel = 5
speed = 100
position = 0
# OSC out/in
sendPort = 7000
sendIP = "127.0.0.1"
receivePort = 7001
receiveIP = "0.0.0.0"
# motor link via Dynamixel U2D2 board
serialPort = "COM3"
motorID = 1
protocol = 2

# OSC address callback
def goal_affect(unused_addr, args, goal):
    motor.set_position(goal)

def accel_affect(unused_addr, args, accel):
    motor.set_acceleration(accel)

def speed_affect(unused_addr, args, speed):
    motor.set_velocity(speed)

def go_affect(unused_addr, args, go):
    pos = motor.get_position()
    client.send_message("/position", pos)


# main program as script
if __name__ == "__main__":
    # OSC address dispatcher
    dispatcher = Dispatcher()
    dispatcher.map("/goal", goal_affect, "rien")
    dispatcher.map("/accel", accel_affect, "rien")
    dispatcher.map("/speed", speed_affect, "rien")
    dispatcher.map("/go", go_affect, "rien")
    # connect to serial
    dxl_io = dxl.DynamixelIO(serialPort)
    # connect to motor
    motor = dxl_io.new_mx64(motorID, protocol)
    # LED off
    motor.write_control_table("LED", 0)
    # enable movement
    motor.torque_enable()
    # motor init
    motor.set_velocity(speed)
    motor.set_acceleration(accel)
    motor.set_position(goal)
    # create OSC output
    client = udp_client.SimpleUDPClient(sendIP, sendPort)
    # create OSC input
    server = osc_server.ThreadingOSCUDPServer((receiveIP, receivePort), dispatcher)
    # wait for incoming OSC
    server.serve_forever()