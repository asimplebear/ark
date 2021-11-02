#!/usr/bin/python3

import pyperclip, json, pprint

st = pyperclip.paste()

pyob = json.loads(st)

pretty = json.dumps(pyob, indent=2, sort_keys=True)

pyperclip.copy(pretty)
