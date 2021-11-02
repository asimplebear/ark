#!/usr/bin/python3

import time
import os

player = 'mplayer'
hr_path = os.path.abspath('sounds/chime-{}.wav')
quarter = os.path.abspath('sounds/chime-one-quarter.wav')
half = os.path

t = time.localtime()

m = t.tm_min
h = t.tm_hour

if m == 15:
    os.system('mplayer /home/moobles/grandfather/sounds/chime-one-quarter.wav')
elif m==30:
    os.system('mplayer /home/moobles/grandfather/sounds/chime-one-half.wav')
elif m==45:
    os.system('mplayer /home/moobles/grandfather/sounds/chime-three-quarter.wav')

else:
    os.system(' '.join([player, hr_path.format(h%12)]))
