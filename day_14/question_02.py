# https://www.acmicpc.net/problem/1003

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    zero = [1, 0]
    one = [0, 1]

    n = int(sys.stdin.readline())
    if n <= 1:
        print(zero[n], one[n])
    else:
        length = len(zero)
        for i in range(length, n+1):
            zero.append(zero[i-2] + zero[i-1])
            one.append(one[i-2] + one[i-1])
        print(zero[-1], one[-1])