from datetime import *
s = input().strip()

temp2 = datetime.strptime(s, '%I:%M:%S%p')
print(temp2.time())