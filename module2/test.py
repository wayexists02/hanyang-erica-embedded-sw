
from ev3dev2.motor import MoveTank, MediumMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_2, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from time import sleep
import sys

mt = MoveTank(OUTPUT_B, OUTPUT_C)
m = MediumMotor(OUTPUT_D)
c = ColorSensor(INPUT_2)


for j in range(5):
    for i in range(9):
        print(c.rgb)
        #sleep(2)
        m.on_for_degrees(100, 53)
    mt.on_for_degrees(10, 10, 38)
    sleep(0.5)
    m.on_for_degrees(-100, 53*9)



'''
for i in range(9):
    mt.on_for_degrees(int(sys.argv[3]), int(sys.argv[3]), int(sys.argv[4]))
    sleep(2)
'''
'''
print("Ready")
t = TouchSensor(INPUT_4)
t.wait_for_pressed()
print("pressed")

'''
mt.stop()

m.stop()
