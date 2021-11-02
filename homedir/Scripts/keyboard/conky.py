#!/usr/bin/python3

import os


def get_note_list():

    l = os.listdir('/home/tbear/Scripts/keyboard/conky-notes')
    l.remove('conky-notes.txt')
    l.remove('index.txt')
    l.sort()

    fob = open('/home/tbear/Scripts/keyboard/conky-notes/index.txt', 'r')
    indy = int(fob.read())
    fob.close()

    return indy, l

def cycle():

    indy, l = get_note_list()

    fob = open('/home/tbear/Scripts/keyboard/conky-notes/{}'.format(l[indy]), 'r')
    st = fob.read()
    fob.close()

    fob = open('/home/tbear/Scripts/keyboard/conky-notes/conky-notes.txt', 'w')
    fob.write(st)
    fob.close()

    indy = (indy+1)%(len(l))

    fob = open('/home/tbear/Scripts/keyboard/conky-notes/index.txt', 'w')
    fob.write(str(indy))
    fob.close()

fob = open('/home/tbear/q', 'a')
fob.write('pop')
fob.close()
#print(get_note_list())
cycle()
