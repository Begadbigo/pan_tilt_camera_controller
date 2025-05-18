from machine import Pin, PWM
from time import sleep
class Servo:
    def __init__(self, servo_pin: int):
        self.__pwm = PWM(Pin(servo_pin, Pin.OUT), freq=50)
        self.current_angle = 90
        self.min_angle = 0
        self.max_angle = 180
        self.min_time = 0.5
        self.max_time = 2.5
        
        self.motor_speed = 60 / 0.1
    def move(self,angle):
        if not self.min_angle <= angle <= self.max_angle:
            return
        slope = (self.max_time - self.min_time) / (self.max_angle - self.min_angle)
        time_per_angle = (angle * slope)  + self.min_time
        duty_cycle = time_per_angle / 20
        pwm_value = duty_cycle * (2**10 -1)
        self.__pwm.duty(int(pwm_value))

        delta_angle = abs(angle - self.current_angle)
        time_delay = delta_angle / self.motor_speed
        time_delay = max(time_delay,0.02)
        
        self.current_angle = angle
        sleep(time_delay)
        
    # Move the servo to the requested angle
    def goto(self, angle):
        self.move(angle)

    # Move the servo to the left, the requested angle
    def left(self, angle):
        target_angle = self.current_angle - angle
        self.move(max(target_angle, self.min_angle))

    # Move the servo to the right, the requested angle
    def right(self, angle):
        target_angle = self.current_angle + angle
        self.move(max(target_angle, self.min_angle))
    