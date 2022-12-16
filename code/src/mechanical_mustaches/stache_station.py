from machine import Pin
from neopixel import NeoPixel
import uasyncio as asyncio


class StacheStation:
    def __init__(self, *, hbt_led, function_button, neo_status, **kwargs):
        self.hbt_led = Pin(hbt_led, Pin.OUT)
        self.function_button = Pin(function_button, Pin.IN)
        self.neo = NeoPixel(Pin(neo_status, Pin.OUT), 1)
        self.neo[0] = (0,0,0)
        self.neo.write()


    def check(self):
        if not self.function_button.value():
            print('function button pressed')
            self.neo[0] = (4,12,0)
            self.neo.write()
            raise KeyboardInterrupt
        
    async def hbt(self):
        while True:
            self.hbt_led.value(not self.hbt_led.value())
            await asyncio.sleep_ms(500)
        
    def fill(self, r, g, b):
        self.neo[0] = (r,g,b)
        self.neo.write()
        
    
class FakeStation:
    def __init__(self):
        pass
    
    def check(*args, **kwargs):
        pass
    
    def fill(*args, **kwargs):
        pass

    