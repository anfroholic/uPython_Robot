import mechanical_mustaches as mm

import socket
import utime
import uasyncio as asyncio


class UDP_Client:
    def __init__(self, *, host: str, port: int):
        self.server = (host, port)
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.s.connect((host, port))
        self.s.bind((mm.my_ip, 8122))
        self.s.setblocking(False)

    async def check(self):
        while True:
            try:
                msg = self.s.recvfrom(100)
                print(msg)
            except OSError:
                pass
            
            await asyncio.sleep_ms(0)
        
    def send(self, msg):
        # print(self.rts, msg, self.queue)
        self.s.sendto(msg, self.server)
