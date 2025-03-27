from machine import Pin, PWM
from micropython_servo_pdm_360 import ServoPDM360RP2Async, SmoothLinear
from time import sleep

# create a PWM servo controller (21 - pin Pico)
servo_pwm = PWM(Pin(21))
# servo_pwm = PWM(Pin(15))

# Set the parameters of the servo pulses, more details in the "Documentation" section
freq = 50
min_us = 400
max_us = 2550
dead_zone_us = 150

# create a servo object
servo = ServoPDM360RP2Async(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

sleep(3)


servo.turn_cv(100)
sleep(0.24 * 2)
servo.stop()
sleep(3)
servo.turn_ccv(900)
sleep(0.24)
servo.stop()

# EMPTY
# servo.turn_cv(1)
# sleep(0.24)
# servo.stop()
# sleep(3)
# servo.turn_ccv(9)
# sleep(0.24)
# servo.stop()
