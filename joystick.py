from machine import Pin, ADC

class Joystick:
    def __init__(self, xAxis: int, yAxis: int, sel: int, mode: str):
        """
        Initialize the joystick.
        
        :param xAxis: GPIO pin for the x-axis (horizontal).
        :param yAxis: GPIO pin for the y-axis (vertical).
        :param sel: GPIO pin for the select button.
        :param mode: Operating mode ("interrupt" or "polling").
        """
        # Initialize ADC for x and y axes
        self.xAxis = ADC(Pin(xAxis))
        self.yAxis = ADC(Pin(yAxis))
        self.xAxis.atten(ADC.ATTN_11DB)  # Set attenuation to 11dB for full 0-3.3V range
        self.yAxis.atten(ADC.ATTN_11DB)  # Set attenuation to 11dB for full 0-3.3V range
        
        # Initialize the select button as an input pin with pull-up
        self.sel = Pin(sel, Pin.IN, Pin.PULL_UP)
        
        # Store the operating mode
        self.mode = mode
        
        # Global variables to store joystick state
        self.joystick_state = {'x': 2048, 'y': 2048, 'button': 'released'}
        
        # Configure interrupt if mode is "interrupt"
        if self.mode == "interrupt":
            self.sel.irq(trigger=Pin.IRQ_FALLING, handler=self.__button_isr)

    def __button_isr(self, pin):
        """
        Interrupt Service Routine (ISR) for the joystick button.
        """
        # Update the button state
        self.joystick_state['button'] = 'pressed'
        

    def reset_button(self):
        """
        Reset the button state to 'released'.
        """
        self.joystick_state['button'] = 'released'

    def read(self):
        """
        Read the joystick state.
        
        :return: The joystick direction ('L', 'R', 'U', 'D', 'M').
        """
        # Read the x and y values (polling)
        x_value = self.xAxis.read()
        y_value = self.yAxis.read()
        
        # Update the joystick state
        self.joystick_state['x'] = x_value
        self.joystick_state['y'] = y_value
        
        
        # Determine the joystick direction
        if self.joystick_state['button'] == 'pressed':
            return 'M'
        elif x_value < 2048:
            return 'R'
        elif x_value > 2048:
            return 'L'
        elif y_value < 2048:
            return 'D'
        elif y_value > 2048:
            return 'U'
        else:
            return 'M'

    def buttonn(self):

        if self.mode == "interrupt":
            # Return the button state without resetting it
            return self.joystick_state['button']
        else:
            return 'pressed' if self.sel.value() == 0 else None