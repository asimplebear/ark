#!/usr/bin/python3

import pyperclip


ugly = pyperclip.paste()


from bs4 import BeautifulSoup as BS
#root = lh.tostring(ugly) #convert the generated HTML to a string
soup = BS(ugly)                #make BeautifulSoup
pretty = soup.prettify()   #prettify the html

#########################
print(pretty)
#########################

pyperclip.copy(pretty)
