n = int(input().strip())
s = input().strip()
t = input().strip()
count = 0
for i in range(n):
    if s[i]==t[i] or s[i]=='.':
        count+=1
    temp = len(s)-count

print(temp)

