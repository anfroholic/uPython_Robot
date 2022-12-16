from machine import ADC, Pin

class Knob:
    def __init__(self, pin:int, atten=ADC.ATTN_11DB, name='corn'):
        self.pin = ADC(Pin(pin), atten=atten)
        self.name = name
        
    
    def read(self) -> float:
        val = self.pin.read_u16()
        return val/65535
        
        