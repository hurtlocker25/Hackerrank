'''
Text wrap module has to convenient functions
1. textwrap.wrap() 
Wraps a single paragraph in text(a string) such that every line is width 
characters long at the most. Returns a list of output lines
 
2. Textwrap.fill()
Wraps a single paragraph in text and returns a single string containing the 
wrapped paragraph 

'''

import textwrap
def wrap(string, max_width):

    temp = textwrap.fill(string, max_width)
    print(temp, end='')

    holder = ''
    return holder

