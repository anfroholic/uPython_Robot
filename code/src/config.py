version = '1.4'
wally = {
    'name': 'wally',
    'louie' : {
        'f_pin': 12,
        'r_pin': 26,
        'freq': 20000,
        'name': 'louie',
        'inverted': True,
        'clamp': (675, 1023)
        },
    'roger': {
        'f_pin': 25,
        'r_pin': 33,
        'freq': 20000,
        'name': 'roger',
        'inverted': True,
        'clamp': (675, 1023)
        }
    }

nemo = {
    'name': 'nemo',
    'pin': 15,
    'num_pix': 5
    }

stache_station = {
    'hbt_led': 27,
    'function_button': 36,
    'neo_status': 14,
    'enable': True
    }



mustache = {
    'name': 'mustache',
    'l_pin': 19,
    'r_pin': 21,
    }

# mustache = {
#     'name': 'mustache',
#     'l_pin': 19,
#     'l_min': 200,
#     'l_max': 520,
#     'r_pin': 21,
#     'r_min': 200,
#     'r_max': 520
#     }


port_A = {
    'A' : 23,
    'B': 22,
    'C': 21,
    'D': 19
    }

port_B = {
    'A' : 17,
    'B': 5,
    'C': 18,
    'D': 13
    }

port_C = {
    'A' : 32,
    'B': 35,
    'C': 34,
    'D': 39
    }

lcd = {
    'sda': 23,
    'scl': 22
    }
