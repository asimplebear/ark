#!/usr/bin/python3

"""
copy contents of first arg file to clipboard
"""

import sys
import pyperclip

if __name__ == '__main__':

    with open(sys.argv[1], 'r') as fob:

        st = fob.read()
        pyperclip.copy(st)
