
A = set(input().split())
n = int(input())
mainlist = []
for i in range(n):
    S1 = set(input().split())
    mainlist.append(S1)
booleantemp = []
for j in mainlist:
    if A.issuperset(j):
        booleantemp.append(True)
    else:
        booleantemp.append(False)

if all(booleantemp)=='True':
    print('True')
else:
    print('False')
