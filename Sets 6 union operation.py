#returns union of a set and set of elements in an iterable
'''
sometimes, | operator used in place of .union() operator; operates only on set of elements
in set. 

Set is immutable to .union() operation or | operation 
'''
# find total number of students who have subscribed to atleast one newspaper
a = int(input())
b = input().split()
temp1 = set(b)

m = int(input())
n = input().split()
temp2 = set(n)

final = temp1.union(temp2)
print(len(final))


