# https://www.acmicpc.net/problem/1874

import sys

n = int(sys.stdin.readline())

sequence = []
for i in range(n):
    sequence.append(int(sys.stdin.readline()))

stack = []
cur_num = 1
result = ''
for i in range(n):
    while cur_num <= sequence[i]:
        stack.append(cur_num)
        cur_num += 1
        result += '+'
    
    if stack[-1] == sequence[i]:
        stack.pop()
        result += '-'
    else:
        print('NO')
        break
else:
    for i in result:
        print(i)