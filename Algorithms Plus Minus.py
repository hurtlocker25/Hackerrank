n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
countplus = 0
countzero = 0
countneg = 0
for values in arr:
    if values==0:
        countzero+=1
    elif values>0:
        countplus+=1
    elif values<0:
        countneg+=1
print(countplus/len(arr))
print(countneg/len(arr))
print(countzero/len(arr))
