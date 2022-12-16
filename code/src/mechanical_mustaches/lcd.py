# MicroPython SSD1306 OLED driver, I2C and SPI interfaces

import time
import framebuf
from machine import SoftI2C, Pin
import mechanical_mustaches.utilities.ssd1306 as ssd1306


class LCD:
    def __init__(self, lcd_sda, lcd_scl):
        self.i2c = SoftI2C(scl=Pin(lcd_scl), sda=Pin(lcd_sda), freq=400000)
        self.initted = False
        if 60 in self.i2c.scan():
            self.lcd = ssd1306.SSD1306_I2C(width=128, height=64, i2c=self.i2c, addr=0x3c, external_vcc=False)
            self.initted = True
        self.buf = []

    def print(self, line: str):
        line_height = 9
        num_lines = 7
        if not self.initted:
            return
        self.lcd.fill(0)
        self.buf.append(line[:16])
        if len(self.buf) > num_lines:
            self.buf.pop(0)
        for row, line in enumerate(reversed(self.buf)):
            self.lcd.text(line, 2, row * line_height)
        self.lcd.show()
    
    def clear(self):
        if not self.initted:
            return
        self.lcd.fill(0)
        self.lcd.show()
        self.buf = []

