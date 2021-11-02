#!/usr/bin/python3

kbpath = "/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml"

import xml.etree.ElementTree as ET
tree = ET.parse('xfce4-keyboard-shortcuts.xml')
#tree = ET.parse(kbpath)
root = tree.getroot()
l0 = [_.attrib for _ in root[0][1]]
l1 = [_.attrib for _ in root[1][1]]


this = l0 + l1





for i in this:

    keypress = i['name'].replace('Primary', 'Pri')
    keypress = keypress.replace('Delete', 'Del')
    keypress = keypress.replace('Super', 'Sup')
    keypress = keypress.replace('Control', 'Ctl')
    keypress = keypress.replace('Shift', 'Sft')
    keypress = keypress.replace('slash', '?')


    keypress = keypress + ' '*(25-len(keypress))

    action = i['value']
    path = '/home/tbear/Scripts/keyboard'
    action = action.replace(path, 'path')

    print('{} ==> {}'.format(keypress, action))


