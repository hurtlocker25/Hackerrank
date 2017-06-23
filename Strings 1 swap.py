# easy way out
'''
def swap_case(s):
    return s.swapcase()

# upper returns a copy of the string in which all case-based characters are upper cased.
'''
def swap_case(s):
    sentence = s.split(' ')
    newstring = [] # new string is a list defined which would then be converted to string as output
    for i in range(0, len(s)):
        letter = s[i]
        if letter.isupper()==True:
            letter= letter.lower()
            newstring.append(letter)
        else:
            letter = letter.upper()
            newstring.append(letter)
    final = ''.join(newstring)   # to get a string from a list
    return final

