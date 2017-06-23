'''
# range(int(input())):
n = int(input())
builtlist = []
temp = []
names = []
for i in range(0, n):
    name = input()
    score = float(input())
    builtlist.append([name, score])

#temp = list(set([x[1] for x in builtlist]))
#secondsmall = sorted(temp)[1]
secondsmall = sorted(list(set([x[1]for x in builtlist])))[1]

for j in range(len(builtlist)):
    if (builtlist[j][1]==secondsmall):
        names.append(builtlist[j][0])
 finallist= sorted(names)
print(*finallist, sep = "\n")
'''

import heapq
# range(int(input())):
n = int(input())
builtlist = []
temp= []
names = []
finallist = []
for i in range(0, n):
    name = input()
    score = float(input())
    builtlist.append([name, score])

    #temp = sorted(builtlist, key = lambda x: x[1])
    #minvalue = min(temp, key= lambda x: x[1])
temp = sorted(list(set([x[1] for x in builtlist])))
secondsmall = heapq.nsmallest(2, temp)[-1]
# temp = list(set([x[1] for x in builtlist]))
# secondsmall = sorted(temp)[1]

for j in range(len(builtlist)):
    if (builtlist[j][1]==secondsmall):
        names.append(builtlist[j][0])
final = sorted(names)
print(*final, sep = "\n")

