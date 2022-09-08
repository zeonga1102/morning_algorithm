# https://www.acmicpc.net/problem/2231

import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    num = list(map(int, str(i)))
    if i + sum(num) == n:
        print(i)
        break
else:
    print(0)