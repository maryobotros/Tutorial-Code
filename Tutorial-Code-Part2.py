from mindstorms import MShub, Motor, Motorpair, ColorSensor, DistcanceSensor, App
from mindstroms.control import wait_for_seconds, wait_until, Timer 
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math 

# Create your objects here 
hub = MSHub()
movement_motors = MotorPair('A', 'B')
distance_sensor = DistanceSensor('D')
lifting_arm = Motor('C')


# Write your program here 
hub.speaker.beep()
lifting_arm.run_to_posotion(0, 'shortest path', 10)
movement_motors.set_default_speed(30)
movement_motors.start()
distance_sensor.wait_for_distance_closer_than(7, 'cm')
movement_motors.stop()
lifting_arm.run_to_posotion(270, 'shortest path', 10)

# Turn to the right
movement_motors.move(20, 'cm', 60)

