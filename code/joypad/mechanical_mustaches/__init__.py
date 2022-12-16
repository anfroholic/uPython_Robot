from mechanical_mustaches.udp_client import UDP_Client
from mechanical_mustaches.timer import Timer
from mechanical_mustaches.auto import Auto
from mechanical_mustaches.button_cb import Button_CB
from mechanical_mustaches.joystick_cb import Joystick_CB

my_ip = None

def wifi_connect(*args):
    print('begin wifi')
    import network
    import utime
    import machine
    import utime
    global my_ip
    if args:
        print('wifi: station mode')
        
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            if len(args) >  1:
                _ssid, password = args
                wlan.connect(_ssid, password)
            else:
                wlan.connect(args[0])
        while not wlan.isconnected():
            utime.sleep(.5)
            print('.', end='')
        print('.')
        my_ip = wlan.ifconfig()[0]
    else:

        letters = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz23456789"
        id = list(machine.unique_id())
        ap_name = 'mustache-' + ''.join([letters[l % len(letters)] for l in id])
        print('creating access point')
        print(f'ap name: {ap_name}')
        ap = network.WLAN(network.AP_IF) # create access-point interface
        utime.sleep_ms(100)
        ap.config(essid=ap_name) # set the SSID of the access point
        utime.sleep_ms(100)
        ap.active(True)         # activate the interface
        my_ip = ap.ifconfig()[0]
    print(f'my ip address is: {my_ip}')

