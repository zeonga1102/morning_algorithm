# https://www.acmicpc.net/problem/1011

# 시간 초과

import sys
sys.setrecursionlimit(100000)

count = 0

def calc_count(dept, dest, pre):
    global count
    
    count += 1
    if dest - dept == 1:
        return True

    if dept >= dest:
        count -= 1
        return False

    if calc_count(dept+pre+1, dest, pre+1):
        return True
    if pre > 0:
        if calc_count(dept+pre, dest, pre):
            return True
    if pre > 1:
        if calc_count(dept+pre-1, dest, pre-1):
            return True
    

t = int(sys.stdin.readline())

for i in range(t):
    count = 0

    x, y = map(int, sys.stdin.readline().split())

    calc_count(x, y, 0)
    print(count)