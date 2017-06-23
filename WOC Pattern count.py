#!/bin/python3

import sys
import re
q = int(input().strip())
cnt = 0
for a0 in range(q):
    s = input().strip()
# matches = re.search('10+1$', s)
    print(len(re.findall('(?=(10+?1))', s)))


#result = [(match.group(1)) for match in temp]

