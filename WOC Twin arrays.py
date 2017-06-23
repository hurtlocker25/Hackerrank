#!/bin/python3
import sys
import itertools
n = int(input().strip())
ar1 = list(map(int, input().strip().split(' ')))
ar2 = list(map(int, input().strip().split(' ')))
min1 = min(ar1)
min2 = min(ar2)
if ar1.index(min1)!=ar2.index(min2):
    print(min1+min2)
elif ar1.index(min1)==ar2.index(min2):
    temp1 = sorted(ar1)[1]
    temp2 = sorted(ar2)[1]
    print(min(min1+temp2, min2+temp1))






#temp = [i+j for i in ar1 for j in ar2 if ar1.index(i)!=ar2.index(j)]

    # result = i+j


'''
sumvalues = []
for i in ar1:
    for j in ar2:
        if ar1.index(i)!=ar2.index(j):
            temp = i+j
            sumvalues.append(temp)
print(min(sumvalues))

# result = twinArrays(ar1, ar2)
#print(result)
'''
