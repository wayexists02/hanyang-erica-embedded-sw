#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from time import sleep, time

on = True

m1 = LargeMotor(OUTPUT_B)
m2 = LargeMotor(OUTPUT_C)
cs1 = ColorSensor(INPUT_1)
cs2 = ColorSensor(INPUT_4)
btn = Button()
snd = Sound()
dis = Display()

green = False
green_time = None

dis.clear()
dis.text_pixels("Ready")
dis.update()

while btn.any() is False:
    sleep(0.1)
snd.beep()

prev_c1 = -1.0
prev_c2 = -1.0

m1.run_forever(speed_sp=300)
m2.run_forever(speed_sp=300)

try:
    while on:
        color1 = cs1.color
        color2 = cs2.color
        #rgb1 = cs1.rgb
        #rgb2 = cs2.rgb

        #print(rgb1, rgb2)

        if green is False and (color1 == 3 or color2 == 3):
            m1.stop()
            m2.stop()
            if green_time is None:
                green_time  = time()

            if time() >= green_time + 3:
                green = True
        elif (color1 == 5 or color2 == 5):
            break
        else:
            c1 = cs1.reflected_light_intensity / 100
            c2 = cs2.reflected_light_intensity / 100
            

            if c1 <= 0.32 and c2 >= 0.48:
                m1.stop(stop_action="brake")
                m2.run_forever(speed_sp=250)
            elif c1 >= 0.48 and c2 <= 0.32:
                m2.stop(stop_action="brake")
                m1.run_forever(speed_sp=250)
            elif c1 > 0.32 and c1 < 0.48 and c2 > 0.32 and c2 < 0.48:
                m1.run_forever(speed_sp=250)
                m2.run_forever(speed_sp=250)

            prev_c1 = c1
            prev_c2 = c2

except Exception as e:
    print(e)

m1.stop()
m2.stop()
snd.beep()
