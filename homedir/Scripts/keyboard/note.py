#!/usr/bin/python3

# <ctrl> + n

#appends clipboard contents to this filepath:
filepath = '/home/tbear/Documents/notes.txt'


import pyperclip

cont = pyperclip.paste()

with open(filepath, 'a') as fob:
    fob.write(cont)
    fob.write("\n")
