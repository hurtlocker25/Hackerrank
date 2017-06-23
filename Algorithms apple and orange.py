s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
countapple = 0
countorange = 0
for value in apple:
    tempapple = a + value
        #print(tempapple)
    if tempapple>=s and tempapple<=t:
        countapple+=1
for value in orange:
    temporange = b + value
    if temporange>=s and temporange<=t:
        countorange+=1
print(countapple, countorange, sep='\n')
