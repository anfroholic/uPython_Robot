"""
Thank you to team 4787, Axiom Robotics
for helping to create this agent

# example setup
larry = agent.LineSensor(
                   name='larry',
                   pins=(32, 35, 34, 39),
                   threshold = 60000,
                   turn_strength = .3
                   )
"""


import mechanical_mustaches as mm
from machine import Pin, ADC
import utime

class LineSensor(mm.Agent):
    def __init__(self, name: str, pins: tuple[int], threshold: int, turn_strength: float):
        super().__init__(name)
        self.sensors = [ADC(Pin(pin), attn=ADC.ATTN_11DB) for pin in pins]
        self.threshold = threshold
        self.turn_str = self.make_turn_strength(turn_strength)
        self.line = 0
        self.dir_vector = 0

    def thresh(self, sensor: ADC) -> None: 
        """read sensor value and return 1 or 0"""
        if sensor.read_u16() > self.threshold:
            return 1
        return 0

    @staticmethod
    def make_turn_strength(mag: float) -> dict[int, float]:  # .3 looks good
        return {0: 0, 1: mag, 3: mag / 2, 2: mag / 3}

    def read(self) -> None:
        line = 0
        for sensor in self.sensors:
            line = line << 1
            line = line | self.thresh(sensor)
        
        self.line = line
        right = self.turn_str[line & 3]
        left = self.turn_str[(line >> 3) | ((line & 4) >> 1)]

        if right > left:
            self.dir_vector = right
        else:
            self.dir_vector = -left
        
        
    def report(self) -> str:
        line = f'{self.line:b}'
        if len(line) < 4:
            line = f"{'0' * (4 - len(line))}{line}"

        return line
    




    
    
