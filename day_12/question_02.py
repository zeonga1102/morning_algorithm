# https://www.acmicpc.net/problem/15650

import sys


def dfs(start):
    if len(sequence) == m:
        for i in sequence:
            print(i, end=' ')
        print()
        return
    
    for i in range(start, n+1):
        if i not in sequence:
            sequence.append(i)
            dfs(i+1)
            sequence.pop()


n, m = map(int, sys.stdin.readline().split())

sequence = []
dfs(1)