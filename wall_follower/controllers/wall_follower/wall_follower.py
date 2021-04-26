"""wall_follower controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 16
max_speed = 10
rot_speed = 6

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
left_motor = robot.getMotor('left wheel motor')
right_motor = robot.getMotor('right wheel motor')
left_motor.setPosition(float('-inf'))
right_motor.setPosition(float('-inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
#  motor = robot.getMotor('motorname')
#  ds = robot.getDistanceSensor('dsname')
#  ds.enable(timestep)
left_sensor = robot.getDevice("left")
left_sensor.enable(timestep)
right_sensor = robot.getDevice("right")
right_sensor.enable(timestep)
middle_sensor = robot.getDevice("middle")
middle_sensor.enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    left_val = left_sensor.getValue()
    right_val = right_sensor.getValue()
    middle_val = middle_sensor.getValue()
    left_speed = max_speed
    right_speed = max_speed
    
    
    if middle_val>999 and left_val > 999 and right_val > 999:
        left_motor.setVelocity(-0.0)
        right_motor.setVelocity(-right_speed)
    
    if middle_val < 900:
        if right_val < 500:
            left_motor.setVelocity(0.0)
            right_motor.setVelocity(-rot_speed)
        if left_val < 500:
            left_motor.setVelocity(-rot_speed)
            right_motor.setVelocity(0.0)
        if right_val > 500 and left_val > 500:
            left_motor.setVelocity(-rot_speed)
            right_motor.setVelocity(0.0)
            
    if middle_val > 900 and (900< left_val < 999) and right_val > 999:
        left_motor.setVelocity(-0.0)
        right_motor.setVelocity(-right_speed)
    if middle_val > 900 and (500< left_val < 900) and right_val > 999:
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(-right_speed)
    if middle_val> 900 and (left_val < 500) and right_val > 999:
        left_motor.setVelocity(-rot_speed)
        right_motor.setVelocity(0.0)
    if middle_val > 900 and (500< right_val < 900) and left_val>999:
        left_motor.setVelocity(-left_speed)
        right_motor.setVelocity(-right_speed)
    
    print(f"left value {left_val}, right value {right_val}, middle value {middle_val}")
# Enter here exit cleanup code.
