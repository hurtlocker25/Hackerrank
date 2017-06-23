# Set is an unordered collection of elements without duplicate entries
# when printed, iterated or converted into a sequence, its elements appear in an arbitrary order

# print set()
# print set('HackerRank')

# sets basically used for membership testing and eliminating duplicate entries
array = int(input())
sumlist = 0
for i in range(array):
    s = input()
    num = map(int, s.split())
    my_list = list(set(num))
    for j in range(len(my_list)):
        sumlist += (my_list[j])
    avg=sumlist/len(my_list)
    print(avg)

## num = map(int, s.split())
        # in python 3, map no longer returns a list
        # num was being stored as a list earlier
        # so use map