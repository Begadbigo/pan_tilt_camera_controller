# Imports
from joystick import Joystick
from servo import Servo
from time import sleep
from machine import Pin

# Variables
servo1 = Servo(servo_pin=23)
servo2 = Servo(servo_pin=22)
servo3 = Servo(servo_pin=2)
servo4 = Servo(servo_pin=4)

joystick = Joystick(xAxis=34, yAxis=35, sel=32, mode='interrupt')

slide_switch = Pin(25, Pin.IN)
led1 = Pin(26, Pin.OUT)
led2 = Pin(27, Pin.OUT)

# Move all servos to 90°
servo1.goto(90)
servo2.goto(90)
servo3.goto(90)
servo4.goto(90)

# Main loop
ans = 1  # Gain value
button_pressed = False

while True:
    # Read the joystick and switch states
    state = joystick.read()
    switch_state = slide_switch.value()
    
    # Check if the joystick button is pressed
    if joystick.buttonn() == 'pressed':
        button_pressed = True
        print("Button pressed! Enter the gain (1-10):")
    
    # Handle gain input if the button is pressed
    if button_pressed:
        try:
            gain = int(input("Enter the gain you want (1-10): "))
            if 1 <= gain <= 10:
                ans = gain
                print(f"Gain set to: {ans}")
                button_pressed = False
                joystick.reset_button()
            else:
                print("Please enter a value between 1 and 10.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Control the LEDs based on the switch state
    if switch_state == 1:
        led1.value(1)
        led2.value(0)
        if state == 'U':
            servo1.left(ans)
        elif state == 'D':
            servo1.right(ans)
        elif state == 'R':
            servo2.left(ans)
        elif state == 'L':
            servo2.right(ans)
    else:
        led1.value(0)
        led2.value(1)
        if state == 'U':
            servo3.left(ans)
        elif state == 'D':
            servo3.right(ans)
        elif state == 'R':
            servo4.left(ans)
        elif state == 'L':
            servo4.right(ans)
    
    # Add a small delay to avoid rapid movements
    sleep(0.1)