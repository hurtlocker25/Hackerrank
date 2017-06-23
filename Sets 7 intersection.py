# returns the intersection of a set and set of elements in an iterable
# & operator used sometimes in place of intersection() operator but it only operates
    # on set of elements in set

# set is immutable to .intersection() operation( or & operation)
a = int(input())
b = input().split()
temp1 = set(b)
m = int(input())
n = input().split()
temp2 = set(n)

final = temp1.intersection(temp2)
print(len(final))



