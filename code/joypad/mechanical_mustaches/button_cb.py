from machine import Pin


class Button_CB:
    def __init__(self, name, pin, pull_up, callback):
        self.name = name
        print(self.name)
        if pull_up:
            self.pin = Pin(pin, Pin.IN, Pin.PULL_UP)
        else:
            self.pin = Pin(pin, Pin.IN)
        self.state = self.pin.value()
        self.callback = callback

    def check(self):
        if self.state != self.pin.value():
            self.state = not self.state
            self.callback(self)