from machine import Pin, PWM
import utime



class Servo:
    # range is 70 --> 650
    def __init__(self, pin: int, *, freq:int=650, min:int= 200, max:int= 1000, name='servo'):
        self.name = name
        self.pin = PWM(Pin(pin), freq=freq, duty=0)
        utime.sleep_ms(10)
        self.pin.init(freq=650, duty=0)
        self.min = min
        self.max = max
        
        utime.sleep_ms(10)
        self.pin.duty(0)
        
        
    def raw(self, duty):
        self.pin.duty(duty)
        
    def set(self, pos):
        """ we want range from -1 to 1 """ 
        duty = self.clamp(pos, -1, 1)
        self.pin.duty(duty)
    
    def degrees(self, deg):
        """ input deg from 0 to 180 """
        duty = self.clamp(deg , 0, 180)
        self.pin.duty(duty)
    
    def clamp(self, val, _min, _max):
        return int(((val - _min) / (_max - _min)) * (self.max - self.min) + self.min)
    
    def report(self):
        return self.pin.duty()
