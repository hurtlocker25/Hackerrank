mystring = input()
kevinscore = 0
stuartscore = 0

vowels = ["a","e","i","o","u"]
for i in range(len(mystring)):
    if mystring[i].lower() in vowels:
        kevinscore+=(len(mystring)-i)
    else:
        stuartscore+= (len(mystring)-i)
if kevinscore>stuartscore:
    print("Kevin", kevinscore)
elif kevinscore<stuartscore:
    print("Stuart", stuartscore)
else:
    print("Draw")

