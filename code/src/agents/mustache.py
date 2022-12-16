import mechanical_mustaches as mm

class Mustache(mm.Agent):
    def __init__(self,
                 driver,
                 name: str,
                 l_pin: int,
                 r_pin: int):
        super().__init__(name)
        self.driver = driver
        self.stachel = mm.Servo(pin=l_pin, name='stachel')
        self.stacher = mm.Servo(pin=r_pin, name='stacher')
        self.state = 'sleeping'
        self.timmy = mm.Timer()
        self.auto = mm.Auto

    
    def check(self):
        states = {
            'sleeping': self.sleeping,
            'dancing': self.auto.check,
            'twisting': self.twisting
            }
        
        states[self.state]()
    
    #-------------------------------------------------------------

    def wiggle(self, pos: float) -> None:
        self.stachel.set(pos)
        self.stacher.set(-pos)
        
    def twist(self, pos: float) -> None:
        self.stachel.set(pos)
        self.stacher.set(pos)
        
    #-------------------------------------------------------------

    def sleep(self):
        self.twist(0)
        self.state = 'sleeping'
        
    def sleeping(self):
        pass
    
    #-------------------------------------------------------------

    def dance(self):
        tiny_dancer = [
            lambda: self.twist(.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(-.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(.75),
            lambda: self.timmy.wait(1),
            lambda: self.twist(-.75),
            lambda: self.timmy.wait(1),
            lambda: self.sleep()
            ]
        self.auto.run(tiny_dancer)
        self.state = 'dancing'
    
    #-------------------------------------------------------------
        
    def twisting(self):
        self.twist(self.driver.get_axis('RX')/2)
        
    def twister(self):
        self.state = 'twisting'
