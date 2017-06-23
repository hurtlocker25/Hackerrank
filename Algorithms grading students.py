n = int(input().strip())
grades = []
grades_i = 0
newgrades = []
for grades_i in range(n):
    grades_t = int(input().strip())
    grades.append(grades_t)
for value in grades:
    if value>=38:
        tempvalue = int(value/5) + 1
        finaltempvalue = tempvalue*5
        if abs(value-finaltempvalue)<3:
            newgrades.append(finaltempvalue)
        elif abs(value-finaltempvalue)>=3:
            newgrades.append(value)
    elif value<38:
        newgrades.append(value)
print(*newgrades, sep='\n')




#print ("\n".join(map(str, result)))


