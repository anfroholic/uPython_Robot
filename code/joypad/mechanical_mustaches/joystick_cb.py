from machine import Pin, ADC

class Joystick_CB:
    def __init__(self, name, pin, callback):
        self.name = name
        print(self.name)
        self.state = None
        self.pin = ADC(Pin(pin))
        self.pin.atten(ADC.ATTN_11DB)
        self.pin.width(ADC.WIDTH_12BIT)
        self.old = self.pin.read() - 32768
        self.callback = callback
    
    def check(self):
        self.state = self.pin.read_u16() - 32768
        if abs(self.state - self.old) > 350:
            self.old = self.state
            self.callback(self)