'''
def print_formatted(number):
    for i in range(1,number+1):
        binlen = len(bin(i)[2:])

        print(str(i).rjust(binlen,' '),end=" "),
        print(str(oct(i)[2:]).rjust(binlen,' '),end=" ")
        print(str(hex(i)[2:].upper()).rjust(binlen,' '),end=" ")
        print(str(bin(i)[2:]).rjust(binlen,' '), sep=' ')
'''
# lesson: Simply use plus to concatenate strings, no need for separate print statements
def print_formatted(number):
    width = len(bin(number)[2:])## used to slice the first 2 characters
    for i in range(1, number + 1):
        print(str(i).rjust(width+1) +
              str(oct(i))[2:].rjust(width + 1) +
              str(hex(i))[2:].upper().rjust(width + 1) +
              str(bin(i))[2:].rjust(width + 1))


# CHECK OUT OTHER SOLUTIONS AS WELL     


