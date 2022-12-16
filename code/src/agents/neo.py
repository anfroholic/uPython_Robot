import mechanical_mustaches as mm
import math
from machine import Pin
from neopixel import NeoPixel

class Neo(mm.Agent):
    
    rbow = tuple([int((math.sin(math.pi / 18 * i) * 127 + 128) / 10) for i in range(36)])
    pink = (10,0,4)
    
    # ------------------------------------------------------------------------
    
    def __init__(self, pin: int, num_pix:int , name: str='nemo'):
        super().__init__(name)
        self.name = name
        pixels = Pin(pin, Pin.OUT)
        self.neo = NeoPixel(pixels, num_pix)
        self.num_pix = num_pix
        self.idx = 0
        self.state = 'sleeping' #rainbow,
        self.auto = mm.Auto()
        self.timmy = mm.Timer()
        
    # ------------------------------------------------------------------------
    
    def fill(self, r, g, b):
        """
        Range is 0 --> 255 for (R,G,B) colors 
        """
        for i in range(self.num_pix):
            self.neo[i] = (r, g, b)
        self.neo.write()
        
    def off(self):
        self.fill(0, 0, 0)
        
    # ------------------------------------------------------------------------
    
    def check(self):
        if self.state == 'sleeping':
            self.sleeping()
        elif self.state == 'rainbowing':
            self.rainbowing()
        elif self.state == 'scrolling':
            self.scrolling()
        elif self.state == 'knightriding':
            self.knightriding()
            
            
    # ------------------------------------------------------------------------
        
    def sleep(self):
        self.off()
        self.state = 'sleeping' 
    
    def sleeping(self):
        pass
        
    # ------------------------------------------------------------------------
    
    def rainbow(self):
        self.state = 'rainbowing'
    
    def rainbowing(self):
        for i in range(self.num_pix):
            index = (self.idx + i*2) % 36
            self.neo[i] = (self.rbow[index], self.rbow[(index + 12)%36], self.rbow[(index + 24)%36])
        self.neo.write()
        self.idx = (self.idx + 1) % 36
    
    # ------------------------------------------------------------------------
    
    def scroll(self, *, speed=.2, color=(10,0,4)):
        self.state = 'scrolling'
        scroller = [
            lambda: self.do_scroll(color),
            lambda: self.timmy.wait(speed)
            ]
        self.auto.run(scroller, loop=True)
        
    def do_scroll(self, color):
        self.idx += 1
        if self.idx >= self.num_pix:
            self.idx = 0
        for p in range(self.num_pix):
            if p == self.idx:
                self.neo[p] = color
            else:
                self.neo[p] = (0,0,0)
        self.neo.write()
        
    def scrolling(self):
        self.auto.check()
        
    # ------------------------------------------------------------------------
    
    def knightride(self, *, speed=.1, color=(10,0,4)):
        self.dir = 'up'
        self.state = 'knightriding'
        knightrider = [
            lambda: self.do_knightride(color),
            lambda: self.timmy.wait(speed)
            ]
        self.auto.run(knightrider, loop=True)
        
    def do_knightride(self, color):
        if self.dir == 'up':
            # print('going up')
            self.idx += 1
            if self.idx >= self.num_pix:
                self.idx = self.num_pix - 2
                self.dir = 'down'
        else: # must be 'down'
            # print('going down')
            self.idx -= 1
            if self.idx <= 0:
                self.dir = 'up'
        
        for p in range(self.num_pix):
            if p == self.idx:
                self.neo[p] = color
            else:
                self.neo[p] = (0,0,0)
        self.neo.write()
        
    def knightriding(self):
        self.auto.check()

