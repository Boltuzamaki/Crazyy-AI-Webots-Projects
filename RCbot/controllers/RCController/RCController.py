"""RCController controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard

# create the Robot instance.
robot = Robot()
keyboard = Keyboard()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
keyboard.enable(timestep)
max_speed = 10

left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    left_speed = max_speed
    right_speed = max_speed
    
    key = keyboard.getKey()
    if (key == ord('W')):
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(-right_speed)
    if (key == ord('S')):
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    if (key==ord('A')):
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(-right_speed)
    if (key==ord('D')):
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(0.0)
    if (key == -1):
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)


# Enter here exit cleanup code.
