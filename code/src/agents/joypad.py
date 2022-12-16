import mechanical_mustaches as mm
from mechanical_mustaches.udp_server import UDP_Server
import struct



def unpack(pack: bytearray) -> tuple[int, int, int, int, int]:
    return struct.unpack('hhhhH', pack[1:])


class Joypad(mm.Agent):
    buttons = {
        'red': 1,
        'blue': 2,
        'yellow': 4,
        'green': 8,
        'start': 16,
        'select': 32,
        'up': 64,
        'down': 128,
        'left': 256,
        'right': 512,
        'l_push': 1024,
        'r_push': 2048
    }

    axises = {
        'LX': 0,
        'LY': 1,
        'RX': 2,
        'RY': 3
    }

    def __init__(self, name: str, port: int = 8122):
        super().__init__(name)
        self.socket = UDP_Server(mm.my_ip, port)
        self.old = (0,0,0,0,0)
        self.state = (0,0,0,0,0)
        self.idx = 0

    def get_but(self, button: str) -> bool:
        return self.buts & self.buttons[button]

    def get_axis(self, axis: str) -> float:
        return self.state[self.axises[axis]]

    def get_but_event(self, button: str) -> None | bool:
        pass


    def check(self):
        self._update()  # this line must be here
        
    
    def disabledPeriodic(self):
        self._update()
    
    def _update(self):
        """update buttons from socket"""
        if self.socket.conn:
            self.old = self.state
            lx, ly, rx, ry, but = unpack(self.socket.jerry) 
            self.state = (lx/32768, ly/32768, rx/32768, ry/32768, but)
        else:
            self.state = (0,0,0,0,0)
                
    def report(self):
        if not self.socket.conn:
            return 'disconnected'
        return f'LX:{self.state[0]:.2f}, LY:{self.state[1]:.2f}, RX:{self.state[2]:.2f}, RY:{self.state[3]:.2f}, b:{self.state[4]:b}'







