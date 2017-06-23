import sys
from functools import reduce
from fractions import gcd
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))

def LCM(a,b):
    return (a*b)//gcd(a,b)
lcm = reduce(LCM, A, 1)
gcd = reduce(gcd, B)

lcm_temp = lcm
count=0
while lcm<=gcd:
    if(gcd%lcm)==0:
        count+=1
    lcm = lcm+lcm_temp
print(count)

