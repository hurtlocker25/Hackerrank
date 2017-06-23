q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    X = list(map(int, input().strip().split(' ')))
    count = 0
    for i in range(1, n-1):
        if X[i]%2==0 and X[i-1]%2==0:
            X[i]=X[i]-1
            X[i+1]=X[i+1]+1
            count+=1
        if X[i]%2!=0 and X[i-1]%2!=0:
            if X[i+1]>1 :
                X[i]=X[i]+1
                X[i+1]=X[i+1]-1
                count+=1
            else:
                count = -1
        if X[i]%2==0 and X[0]%2!=0:
            if X[n-1]%2==0:
                X[i]=X[i]-1
                X[i-1]=X[i-1]+1
                count+=1
            elif X[n-1]%2!=0:
                count = -1
    print(count)


