# returns a set with all elements from set that are not in the iterable
# sometimes '-' operator is used in place of .difference() tool
    # but it only operates on set of elements in set

# set is immutable to .difference() operation
a = int(input())
b = input().split()
temp1 = set(b)
m = int(input())
n = input().split()
temp2 = set(n)
print(len(temp1.difference(temp2)))
