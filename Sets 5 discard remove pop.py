'''
set.remove(x)
removes x from the set. If x does not exist, raises key error. 
.remove(x) operation returns none
 
 set.discard() same as remove but does not return key error

set.pop() removes and returns an arbitrary element from the set 
if no elements to remove, key error raised 
'''
n = int(input())
A = (set(map(int, input().split())))
for item in A:
    while item>0 and item<=9:
        number = int(input())
        for j in range(number):
            commands = input().split()# trick - returns a list
            if commands[0]=="pop":
                A.pop()
            elif commands[0] =="remove":
                A.remove(int(commands[1]))
            elif commands[0] =="discard":
                A.discard(int(commands[1]))


        print(sum(A))
