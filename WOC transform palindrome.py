#!/bin/python3
import sys
n,k, m = input().strip().split(' ')
n,k, m = [int(n),int(k), int(m)]

for a0 in range(k):
    x,y = input().strip().split(' ')
    x,y = [int(x),int(y)]

a = list(map(int, input().strip().split(' ')))
L = [[0 for x in range(m)] for x in range(m)]
for i in range(m):
    L[i][i]=1

    for cl in range(2, m+1):
        for i in range(m-cl+1):
            j = i+cl-1
            if a[i]==a[j] and cl == 2:
                L[i][j]=2
            elif a[i]==a[j]:
                L[i][j]=L[i+1][j-1]+2
            else:
                L[i][j]=max(L[i][j-1], L[i+1][j])
temp = L[0][m-1]
for x in a:
    x = y
