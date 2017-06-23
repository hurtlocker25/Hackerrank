arr = list(map(int, input().strip().split(' ')))

for values in arr:
    temp = sorted(arr)
    minsum = sum(temp[0:4])
    maxsum = sum(temp[1:5])
print(minsum,maxsum)