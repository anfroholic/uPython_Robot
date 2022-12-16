
mustache = (
'   m         mmmmm     mmmmm         m   ',
' mm        mmmmmmmm   mmmmmmmm        mm ',
'mm        mmmmmmmmmm mmmmmmmmmm        mm',
'mm       mmmmmmmmmmmmmmmmmmmmmmm       mm',
'mmm    mmmmm FIRST® Robotics mmmmm    mmm',
'mmmmmmmmmmmmmm Team: 8122 mmmmmmmmmmmmmmm',
' mmmmmmmm Mechanical  Mustaches mmmmmmmm ',
'  mmmmmmmmmmmmmmmmmm mmmmmmmmmmmmmmmmmm  ',
'   mmmmmmmmmmmmmmmm   mmmmmmmmmmmmmmmm   ',
'     mmmmmmmmmmm          mmmmmmmmmm     ')



def mu():
    yield from mustache

stache = mu()




import config
print(f'board version: {config.version}')

# clear error log
with open('/mechanical_mustaches/web/errors.log', 'w') as f:
    f.write('')

print('growing mustache :{D ')
from mechanical_mustaches.motor import Motor
print(next(stache))
from mechanical_mustaches.servo import Servo
print(next(stache))
from mechanical_mustaches.timer import Timer
print(next(stache))
from mechanical_mustaches.auto import Auto
print(next(stache))
from mechanical_mustaches.button import Button
print(next(stache))
from mechanical_mustaches.knob import Knob
print(next(stache))
from mechanical_mustaches.lcd import LCD
print(next(stache))
from mechanical_mustaches.agent import Agent, m
print(next(stache))
from mechanical_mustaches.stache_station import StacheStation
print(next(stache))


def start_web_page():
    print('begin webpage')
    m.ss.fill(10,0,4)
    import mechanical_mustaches.web.index
    m.ss.fill(0,0,0)

m.set_LCD(LCD(config.lcd['sda'], config.lcd['scl']))
print(next(stache))
if config.stache_station['enable']:
    print('enabling ss')
    import uasyncio
    m.ss = StacheStation(**config.stache_station)
    loop = uasyncio.get_event_loop()
    loop.create_task(m.ss.hbt())

def send_file(file):
    with open(f'/mechanical_mustaches/web/static/{file}', 'r') as f:
        return f.read()

my_ip = None

def wifi_connect(*args):
    print('begin wifi')
    import network
    import utime
    import machine
    import utime
    global my_ip
    if args:
        m.post('wifi: station mode')
        m.ss.fill(0,4,0)
        _ssid, password = args
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            wlan.connect(_ssid, password)
        while not wlan.isconnected():
            utime.sleep(.5)
            print('.', end='')
        print('.')
        my_ip = wlan.ifconfig()[0]
    else:
        m.ss.fill(0,4,0)
        letters = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
        id = list(machine.unique_id())
        ap_name = 'mustache-' + ''.join([letters[l % len(letters)] for l in id])
        print('creating access point')
        m.post(ap_name)
        m.post('ap name:')
        ap = network.WLAN(network.AP_IF) # create access-point interface
        utime.sleep_ms(100)
        try:
            ap.config(essid=ap_name) # set the SSID of the access point
        except OSError:
            import machine
            machine.reset()
        utime.sleep_ms(100)
        ap.active(True)         # activate the interface
        my_ip = ap.ifconfig()[0]
    m.ss.fill(0,0,0)
    m.post(my_ip)
    m.post('my ip address is:')
