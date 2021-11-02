#!/usr/bin/python3

#1/0  #squelch it

import time
import os

player = 'mplayer'
chimes = {0  : './sounds/chime-{}.wav',
          15 : './sounds/chime-one-quarter.wav',
          30 : './sounds/chime-one-half.wav',
          45 : './sounds/chime-three-quarter.wav'
         }

t = time.localtime()
hour, minute = t.tm_hour%12, t.tm_min

peal = ' '.join([player, os.path.abspath(chimes[minute]).format(hour)])

os.system(peal)

