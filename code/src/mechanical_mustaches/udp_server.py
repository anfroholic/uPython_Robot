"""
used with Jerry Joypad
"""
import socket
import uasyncio
import utime






class UDP_Server:
    def __init__(self, address: str, port: int, check_in_interval: int=1000):
        self.addr = address
        self.port = port
        
        # set up socket
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.setblocking(False)
        self.s.bind((address, port))

        self.raw = b''
        self.jerry = b''
        
        self.conn = None
        self.checkin = 0
        self.ch_int = check_in_interval

        loop = uasyncio.get_event_loop()
        loop.create_task(self.check())
        loop.create_task(self.hbt())


    async def check(self):
        while True:
            try:
                data, addr = self.s.recvfrom(1024)  # buffer size is 1024 bytes
                self.conn = addr
                if data[0] == 2: # joypad package
                    self.jerry = data
                # print(f"received message: {data}")
                self.conn = addr
                self.checkin = utime.ticks_ms()
                
            except OSError:
                pass

            await uasyncio.sleep_ms(0)
            
    
    async def hbt(self):
        """check controller is still active"""
        while True:
            if not self.conn:
                 pass

            elif utime.ticks_diff(utime.ticks_ms(), self.checkin) > self.ch_int:
                print('closing connection')
                self.conn = None
                
            await uasyncio.sleep_ms(100)
    
    def send(self, msg: str) -> None:
        if self.conn:
            self.s.sendto(msg, self.conn)
