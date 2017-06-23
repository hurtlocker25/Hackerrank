'''
********No idea python sets hackerrank*****
Set A - Like all integers 
Set H - Dislike all integers
'''

n, m = input().split()
happiness = 0
happinessA = 0
happinessB = 0
arr = (set([int(x) for x in input().split()]))
A = set([int(y) for y in input().split()])
B = set([int(z) for z in input().split()])
count = [1 if x in A else -1 if x in B else 0 for x in arr]
print(sum(count))


'''
Another method - list comprehensions 

n, m = input().split()
arr = input().split()
A = set(input().split))
B = set(input().split())

print(sum([(item in A) - (item in B) for item in arr]))


'''