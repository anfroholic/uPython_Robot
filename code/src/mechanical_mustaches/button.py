from machine import Pin

class Button:
    def __init__(self, pin:int, name='button', inverted=True):
        self.pin = Pin(pin, Pin.IN)
        self.name = name
        self.inverted = inverted
        
        
    def read(self):
        val = self.pin.value()
        if self.inverted:
            return not val
        return val
        
        
    
        
    
        



