# https://www.acmicpc.net/problem/1002

# 0: 두 점 사이 거리가 반지름의 합보다 작을 때, 둘의 좌표가 같고 반지름이 다를 때, 한 원이 다른 원의 안에 포함될 때
# 1: 두 점 사이 거리가 반지름의 합과 같을 때(외접할 때), 내접할 때
# -1: 둘의 좌표와 반지름이 같을 때
# 2: 그 외

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue

    distance_sqr = (x1 - x2)**2 + (y1 -y2)**2
    r_sum_sqr = (r1 + r2)**2
    if distance_sqr == r_sum_sqr:
        print(1)
    elif distance_sqr > r_sum_sqr:
        print(0)
    elif distance_sqr == (r1 - r2)**2:
        print(1)
    elif distance_sqr**0.5 + min(r1, r2) < max(r1, r2):
        print(0)
    else:
        print(2)