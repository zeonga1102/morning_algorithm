# https://www.acmicpc.net/problem/1541

import sys

formula = sys.stdin.readline().strip().split('-')
result = 0

num_list = formula[0].split('+')
for i in num_list:
    result += int(i)

for i in formula[1:]:
    cur = 0
    num_list = i.split('+')
    for j in num_list:
        cur += int(j)
    
    result -= cur

print(result)