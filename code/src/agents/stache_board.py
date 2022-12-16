'''
use this document to create new buttons on the shuffleboard

'''
from robot import *


# fill in this dictionary with names and functions to add to webpage

print('IMPORTING STACHEBOARD')

buttons = {
    'nemo.sleep()': lambda: nemo.sleep(),
    'nemo.rainbow()': lambda: nemo.rainbow(),
    'nemo.scroll()': lambda: nemo.scroll(),
    'nemo.knightride()': lambda: nemo.knightride(),
    'stache.twister()': lambda: stache.twister()
}
