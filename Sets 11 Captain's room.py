# the captain's room

k = int(input())
tourists = input().split()

temp = set(tourists)
num_of_groups = int(len(tourists)/k)

for i in temp:
    if tourists.count(i)==1:
        print(i)

