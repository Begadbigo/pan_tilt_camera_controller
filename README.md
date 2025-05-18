# Pan & Tilt Camera Controller - ESP32 (MicroPython)
*Graduation project from DECI L4 Semester 1*

A MicroPython-based project for ESP32 to control a dual-camera pan & tilt system using joystick input, servo motors, slide switches, and LEDs.

## Project Overview

This project allows real-time control of two cameras using a joystick and 4 servos (two per camera). The direction is based on analog joystick readings, while a slide switch toggles control logic. Additional user-defined gain values adjust movement sensitivity. LEDs reflect switch states, and interrupt-driven mechanisms ensure responsiveness and efficiency.

## Features

- **Joystick Direction Detection**  
  - Analog reading via ADC in polling or interrupt mode  
  - Outputs one of: `'U'`, `'D'`, `'L'`, `'R'`, or `'M'` (Middle)  
  - Button press triggers a prompt for gain entry (1–10) via Serial

- **Servo Motor Control**  
  - 4 Servos (2 per camera) initialized at 90°  
  - Can rotate left/right by set degrees  
  - Controlled using `goto()`, `left()`, and `right()` methods  
  - Servo movement speed is scaled by the user-entered gain

- **Switch and LED Logic**  
  - One slide switch controls logic  
  - LED1 lights up when switch = ON, LED2 lights up when switch = OFF  
  - State read and stored in a dedicated variable

- **Interrupt-Driven Timer**  
  - Joystick module supports interrupt timer mode  
  - Ensures smooth analog input handling without polling in main loop
 
## Technologies Used

- MicroPython
- ESP32 microcontroller
- Wokwi Simulator
- Serial Communication via UART
- PWM-based Servo Control
- Interrupt and Timer handling


## How To Run

1. Upload the code to your ESP32 board using Wokwi or a supported MicroPython IDE.
2. Slide the switch to toggle LED state and control logic.
3. Use the joystick to move camera angles.
4. Press the joystick button to input gain (1–10) from Serial Terminal.
5. Watch the servo motors rotate with speed based on gain.
6. You could run directly from the link below.

*Note: Only one analog sensor (joystick) is connected and used at a time. The system reads from the actual device connected to the input pin, not all devices simultaneously.*

## My Role

I implemented all core functionalities including analog reading, servo motion with gain scaling, hardware interrupt integration, and organized modular Python files for reusability. I also ensured proper circuit layout and responsiveness in the Wokwi simulation environment.

## File Structure

```bash
.
├── main.py         # Main control loop: handles switch, LEDs, joystick button, servo movement
├── joystick.py     # Joystick class: ADC reading, direction detection, optional interrupt handling
├── servo.py        # Servo control class: angle movement, gain integration
```
## Project Links

- [Wokwi Project Link](https://wokwi.com/projects/431301456840524801)  
- [GitHub Repository](https://github.com/Begadbigo/pan_tilt_camera_controller)

