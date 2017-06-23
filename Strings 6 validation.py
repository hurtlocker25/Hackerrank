#python has built in string validation methods.
# can check if string has alphabetical characters, alphanumeric, digits

# str.isalnum() checks if all characters in string are alphanumeric
            # alphanumeric implies a-z, A-Z and 0-9

# str.isaplha() checks if all characters of a string are alphabetical
                    # a-z or A-Z

# str.isdigit() checks if all characters of a string are digits
                    # just 0-9
# str.islower()
# str.isupper()
# need to check if the string has those characters specified above
s = input()

temp = any(i.isalnum() for i in s)
print(temp)
temp1 = any(i.isalpha() for i in s)
print(temp1)
temp2 = any(i.isdigit() for i in s)
print(temp2)
temp3 = any(i.islower() for i in s)
print(temp3)
temp4 = any(i.isupper() for i in s)
print(temp4)

s = input()

for i in s:
    if any(i.isalnum()):
        print(True)



