#import ev3dev.ev3 as ev3
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.motor import OUTPUT_B, OUTPUT_C, MoveTank, SpeedPercent
import time


tank = MoveTank(OUTPUT_B, OUTPUT_C)
tank.cs1 = ColorSensor(INPUT_1)
tank.cs1.mode = "COL-REFLECT"
tank.cs2 = ColorSensor(INPUT_4)
tank.cs2.mode = "COL-REFLECT"

#tank.on_for_degrees(100, 100, 1000)

tank.stop()

try:
    while True:
        
        print("==1==")
        print(tank.cs1.reflected_light_intensity)
        print(tank.cs1.rgb)

        print("==2==")
        print(tank.cs2.reflected_light_intensity)
        print(tank.cs2.rgb)

        print()

        #time.sleep(1)
        

except:
    pass

tank.stop()

