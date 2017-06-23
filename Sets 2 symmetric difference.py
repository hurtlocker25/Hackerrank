# new data type - sets
# inputs given on one line separated by a space character
        # use split to separate values to form list

# if list values are all integer types
'''

use map() method to convert all strings to integers 

a = raw_input()
lis = a.split() 

newlis = list(map(int, lis))

sets ~ an unordered set of unique values. 
single set - contains values of any immutable data type 

1. myset = {1,2} --> directly creating a set 
2. myset = set() --> initializing a set 
3. myset = set(['a', 'b']) --> creating set from a list

using add function:
myset.add('c')
give {'a','b','c'} 

myset.update([1,2,3,4]) only works for iterable objects
myset
{'a', 1, 'c', 'b', 4, 2, (5,4), 3} 

discard() and remove() to delete items 

'''

'''
Union Intersection difference functions
a = {2,4,5,9} 
b = { 2, 4, 11, 12} 
a.union(b) 
{2,4,5,9,11,12} 

a.intersection(b)
{2, 4} 

a.difference(b)
{9, 5} 
UNION and INTERSECTION are symmetric methods 

a.union(b) == b.union(a) 
a.intersection(b) == b.intersection(a)
 
'''
'''
m = int(input())
for i in range(m):
    inputs = list(map(int, input().split()))
    print(inputs)
    n = int(input())
    for j in range(n):
        inputs2 = list(map(int, input().split()))
        print(inputs2)

        setA = set(inputs)
        setB = set(inputs2)

        isdifferenceA= setA.difference(setB)
        isdifferenceB = setB.difference(setA)
        temp = isdifferenceA.union(isdifferenceB)
        #print(isdifferenceA.union(isdifferenceB))
        templist = sorted(list(temp))

        for item in templist:
            print(item)

'''
input()
a=set(map(int,input().split()))
input()
b=set(map(int,input().split()))
c=a.symmetric_difference(b)
for n in sorted(list(c)):
    print(n)







