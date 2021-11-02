#!/usr/bin/python3

'''
togle through conky info pages
'''

conky_path = '/home/tbear/Scripts/conky/conky-notes'
notes_file = 'conky-notes.txt'
notes_path = '{}/{}'.format(conky_path,notes_file)
index_file = 'index.txt'
index_path = '{}/{}'.format(conky_path, index_file)

import os

def get_note_list():

    l = os.listdir(conky_path)
    l.remove(notes_file)
    l.remove(index_file)

    l.sort()

    with open(index_path, 'r') as fob:
        index = int(fob.read())

    return index, l


def increment_index(index, length):
    index = (index+1)%(length)

    with open(index_path, 'w') as fob:

        fob.write(str(index))



def cycle():

    index, l = get_note_list()

    disp_path = '{}/{}'.format(conky_path,l[index])

    try:
        with open(disp_path,'r') as fob:
            st = fob.read()
    except:
        st = '{} not around.  probably broken sym link'.format(disp_path)

    with open(notes_path,'w') as fob:
        fob.write(st)


    increment_index(index, len(l))

if __name__ == '__main__':

    cycle()
