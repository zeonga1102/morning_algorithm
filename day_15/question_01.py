# https://www.acmicpc.net/problem/11866

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
k -= 1
dq = deque([str(i) for i in range(1, n+1)])
p = []

while len(dq) > 0:
    dq.rotate(-k)
    p.append(dq.popleft())

print(f"<{', '.join(p)}>")