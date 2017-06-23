
N = [2, 3, 6, 6, 5]
sortedlist = sorted(N)
temp = len(sortedlist)
emptylist = []

# 2, 3, 5, 6, 6
i = 0
for i in range(0, temp-1):
    while sortedlist[i]<sortedlist[i+1]:
        i+=1
        emptylist.insert(i, sortedlist[i-1])

b = max(emptylist)
print(max(emptylist))










'''for temp in range(2,11):
    for i in sortedlist[i]:
        for sortedlist[i] in range(-100,101):
            if sortedlist[i]
   '''




