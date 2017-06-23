mystring = input()

if list(mystring)==list(reversed(mystring)):
    print("YO, "+mystring+" is a palindrome!")
else:
    print("Nope!")