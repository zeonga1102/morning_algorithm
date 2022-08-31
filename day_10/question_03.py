# https://www.acmicpc.net/problem/1021

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

location = list(map(int, sys.stdin.readline().split()))

dq = deque([i for i in range(1, n+1)])

count = 0
for i in location:
    while dq[0] != i:
        if dq.index(i) < len(dq) / 2:
            while dq[0] != i:
                dq.rotate(-1)
                count += 1
        else:
            while dq[0] != i:
                dq.rotate(1)
                count += 1
    dq.popleft()
    
print(count)