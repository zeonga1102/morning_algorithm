# https://www.acmicpc.net/problem/1260

import sys
from collections import deque


def dfs(v):
    dfs_visited[v] = 1
    print(v, end=' ')
    
    for i in range(1, n+1):
        if dfs_visited[i] == 0 and graph[v][i] == 1:
            dfs(i)


def bfs(v):
    dq = deque()
    dq.append(v)
    bfs_visited[v] = 1

    while dq:
        v = dq.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if bfs_visited[i] == 0 and graph[v][i] == 1:
                dq.append(i)
                bfs_visited[i] = 1


n, m, v = map(int, sys.stdin.readline().split())

graph = [[0] * (n+1) for _ in range(n+1)]
dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

for _ in range(m):
    v1, v2 = map(int, sys.stdin.readline().split())

    graph[v1][v2] = 1
    graph[v2][v1] = 1

dfs(v)
print()
bfs(v)