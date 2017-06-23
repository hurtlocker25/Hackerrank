'''
Use .update() or |= operation to create mutations to a set 
H = set("Hacker")
R = set("Rank") 
H.update(R)
print(H)
'''
'''
.intersection_update() 
Use to update set by keeping only the elements found in it and
iterable/another set
 '''
'''
.symmetric_difference_update() 
'''

'''
.difference_update() 

'''
from decimal import Decimal
n = int(input())
m = input().split()
orig_set = set(m)
a = int(input())
for i in range(a):
    entry = list(input().split())
    if entry[0]=='intersection_update':
        update_set = set(input().split())
        orig_set.intersection_update(update_set)
    if entry[0]=='update':
        update_set = set(input().split())
        orig_set.update(update_set)
    if entry[0] =='symmetric_difference_update':
        update_set=set(input().split())
        orig_set.symmetric_difference_update(update_set)
    if entry[0]=='difference_update':
        update_set = set(input().split())
        orig_set.difference_update(update_set)
print(sum(Decimal(i) for i in orig_set))


