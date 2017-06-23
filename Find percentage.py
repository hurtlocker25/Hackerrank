n = int(input())
student_marks = {}


for i in range(0, n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

    scoreslength = int(len(scores))
    avg = 0

query_name = input()
#while student_marks[query_name]==student_marks[name]:

avg = sum(student_marks[query_name])/scoreslength
print("%.2f" %avg)  # to round the output to two decimal places

