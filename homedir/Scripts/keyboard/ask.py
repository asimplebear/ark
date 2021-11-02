#!/usr/bin/python3

########################################
########################################
#
#           KEY PRESS
#@           <ctrl>+?
#
#@  opens webbrowser and sends contents
#@  of clipboard as query to google
#@######################################

import webbrowser
import pyperclip

base_qstr = 'https://www.google.com?q={}'
what = pyperclip.paste()
qstr = base_qstr.format(what)
webbrowser.open(qstr)



