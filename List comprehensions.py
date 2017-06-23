
#x = int(input())
#y = int(input())
#z = int(input())

# n = int(input())
a = 1
b = 1
c = 1
n = 2

import itertools
# lesson - itertools can be used to invoke effects of a nested for loop

listcomp = [[i,j,k] for i,j,k in itertools.product(range(0, a+1),range(0,b+1), range(0, c+1)) if i+j+k!=n]

# if one wants to just loop simultaneously, can use
    # for i, j in zip(range(x), range(y))

# list comp reference: http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-15--generators-and-list-comprehensions

# itertools python docs - https://docs.python.org/3/library/itertools.html














'''
def calcfunc(m):
    listtemp = []
    current = 1
    while current <= m:
        current += 1
        listtemp.append(cube(current))
    return listtemp
'''




