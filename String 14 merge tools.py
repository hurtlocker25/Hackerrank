string = input()
k = int(input())

n = len(string)
increment = int(n/k)
unique = []
for i in range(0, n, k):
    subsegment = string[i:i + k]
    for j in range(len(subsegment)):
        if subsegment.count(subsegment[j])>1:
            templist = sorted(set(subsegment), key=subsegment.index)
            finalstr = ''.join(templist)

    print(finalstr)
