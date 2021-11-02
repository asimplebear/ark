#!/usr/bin/python3

import os
import time
import _thread
from playsound import playsound as play


print('a')




t = time.localtime()
hour, minute = t.tm_hour, t.tm_min


with open('/home/tbear/grandee.txt', 'a') as fob:
    fob.write(f'time: {hour} {minute}\n')



if minute in [15, 30, 45]:
    #play('/home/tbear/Scripts/grandfather/quarter3.mp3')
    pass
if minute == 0:
    #play('/home/tbear/Scripts/grandfather/quarter3.mp3')
    for i in range(hour):
        #play('/home/tbear/Scripts/grandfather/bongtrail.mp3')
        pass



#play('/home/tbear/Scripts/grandfather/bongtrail.mp3')
print('b')




'''
sounds = sorted(os.listdir('grandfather'))
print(sounds)
for sound in sounds:
    play(f'grandfather/{sound}')
    name = input(f'rename {sound}')
    os.rename(f'grandfather/{sound}', f'grandfather/{name}')
'''

'''
l = os.listdir('grandfather')

for i in l:
    play(f'grandfather/{i}')
'''

"""
from pydub import AudioSegment as AS

sounds = sorted(os.listdir('grandfather'))

for sound in sounds:
    sf = AS.from_file(f'grandfather/{sound}', format='mp3')
    sf = sf - 20
    with open(f'grandfather/{sound}8', 'wb') as fob:
        sf.export(fob, format='mp3')
"""










