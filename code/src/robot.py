import mechanical_mustaches as mm
from mechanical_mustaches import m
from agents import wheels, neo, joypad, mustache
import config
import uasyncio as asyncio



timmy = mm.Timer()
wally = wheels.Wheels(**config.wally)
nemo = neo.Neo(name='nemo', pin=15, num_pix=5)


# driver = joypad.Joypad('jerry')
# stache = mustache.Mustache(driver, **config.mustache)
# timmy = mm.Timer()
# wally = wheels.Wheels(driver, **config.wally)
# nemo = neo.Neo(name='nemo', pin=15, num_pix=5)



class Robot:
    def __init__(self):
        pass
    
    def autonomousInit(self):
        # m.add_auto(wiggles, name='mr_wiggles')
        pass
    
    
    async def autonomousPeriodic(self):
        await m.auto_check()
    
    
    def robotInit(self):
        pass
    
    
    async def robotPeriodic(self):
        pass
    
    
    def testInit(self):
        nemo.sleep()
#        pass
    
    
    async def testPeriodic(self):
        pass
    
    def teleopInit(self):
        pass
    
    
    async def teleopPeriodic(self):
        await m.check()
        
        
    def disabledInit(self):
        nemo.rainbow() 
#       pass
    
    
    async def disabledPeriodic(self):
        await m.disabledPeriodic() 
        nemo.check()
#         pass
        


        
        
        