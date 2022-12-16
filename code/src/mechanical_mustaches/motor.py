from machine import Pin, PWM
import utime



class Motor:
    def __init__(self, f_pin: int, r_pin: int, freq: int, name: str, clamp: tuple[int, int]=None, inverted: bool=False):
        
        self.name = name
        self.f_pin = f_pin
        self.r_pin = r_pin
        self.freq = freq
        self.f = PWM(Pin(f_pin), freq=freq)
        self.r = PWM(Pin(r_pin), freq=freq)
        self.inverted = inverted
        self.clamp = clamp
        utime.sleep_ms(1)
        self.f.duty(0)
        self.r.duty(0)
        
        print("{} has entered the arena".format(self.name))
         
    def intro(self):
        print("My name is {}, my forward pin is {}, my reverse pin is {}, and my frequency is {}. Also mint chocolate chip is the best ice cream flavor.".format(self.name, self.f_pin, self.r_pin, self.freq))

    # + Speed move forward
    # - Speed move backward
    def set(self, speed: float) -> None:
        """
        Range is -1 <---> 1 for Speed
        """
            
        if speed > 0:
            if speed > 1:
                speed = 1
            self.set_raw(int(speed * 1023))
        elif speed < 0:
            if speed < -1:
                speed = -1
            self.set_raw(int(speed * 1023))
        else:
            self.set_raw(0)

    def set_raw(self, speed: int) -> None:
        """
        Range is -1023 <---> 1023 for Speed
        """
        
        if speed != 0:            
            if self.clamp:
                neg = True if speed < 0 else False
                speed = self.do_clamp(abs(speed), 0, 1023)
                if neg:
                    speed = -speed
                
            if self.inverted:
                speed = -speed
        

        if speed > 0:
            self.f.duty(speed)  # forward pin
            self.r.duty(0)  # reverse pin
        elif speed < 0:
            self.f.duty(0)
            self.r.duty(abs(speed))
        else:
            self.f.duty(0)
            self.r.duty(0)

    def report(self):
        return f'f:{self.f.duty()}, r:{self.r.duty()}'
    
    def do_clamp(self, val, _min, _max):
        return int(((val - _min) / (_max - _min)) * (self.clamp[1] - self.clamp[0]) + self.clamp[0])
    