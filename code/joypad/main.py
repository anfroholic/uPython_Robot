import mechanical_mustaches as mm
import struct
import uasyncio
import config
import wifi_cfg

mm.wifi_connect('mustache-RadYSz')

print('I am jerry')

# server = mm.UDP_Client(host='10.203.136.32', port=8122)
# server = mm.UDP_Client(host='10.203.136.55', port=8122)
server = mm.UDP_Client(host='192.168.4.1', port=8122)

from agents import neo

nemo = neo.Neo(15, 5)
nemo2 = neo.Neo(13, 1)

agent_list = [
nemo,
nemo2
]




def print_but(button):
    print(f'{button.name} {not button.state}')

def print_alog(alog):
    print(f'{alog.name} {alog.state}')




# set up hardware
buts = [mm.Button_CB(name, pin, True, print_but) for name, pin in config.buttons]
    
alogs = [mm.Joystick_CB(name, pin, print_alog) for name, pin in config.alogs]

func = mm.Button_CB('func', 36, False, print_but)




def pack_buts() -> int:
    but_pack = 0
    for but in reversed(buts):
        but_pack = but_pack << 1
        but_pack |= int(not but.state)
    return but_pack

def pack_logs() -> list[int]:
    return [log.state for log in alogs]

def pack_all() -> bytearray:
    p = pack_logs()
    p.append(pack_buts())
    return b''.join((b'\x02', struct.pack('hhhhH', *p)))



async def check():
    while True:
        for but in buts:
            but.check()
        for a in alogs:
            a.check()
        # func.check()
        
        await uasyncio.sleep_ms(100)

async def sender():
    while True:
        wait = 20
        try:
            server.send(pack_all())
        except OSError:
            print('no host found')
            wait = 1000
        
        await uasyncio.sleep_ms(wait)

loop = uasyncio.get_event_loop()
loop.create_task(server.check())
loop.create_task(check())
loop.create_task(sender())
loop.run_forever()

