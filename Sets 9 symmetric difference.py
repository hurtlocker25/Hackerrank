# symmetric difference operator returns a set with all elements in the
    # set and are iterable but not both

# sometimes a ^ operator is used in place of symmetric_difference() but
    # it only operates on set of elements in set
a = int(input())
b = input().split()
m = int(input())
n = input().split()

print(len(set(b).symmetric_difference(set(n))))




