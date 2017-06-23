n = int(input().strip())
a = []
temp1 = 0
temp2 = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(n):
    for j in range(n):
        if i==j:
            temp1+=a[i][j]
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            temp2+=a[i][j]
print(abs(temp1-temp2))