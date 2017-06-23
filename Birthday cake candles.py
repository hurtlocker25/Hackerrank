#!/bin/python3

import sys
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
temp = sorted(ar)
count = 0
maxheight = max(temp)
for values in temp:
    if values == maxheight:
        count+=1


#print(result)
