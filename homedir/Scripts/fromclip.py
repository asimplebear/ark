#!/usr/bin/python3

"""
appends contents of clipboard to the filename in first arg
"""

import sys
import pyperclip

if __name__ == '__main__':

    with open(sys.argv[1], 'a') as fob:
        fob.write(pyperclip.paste())
