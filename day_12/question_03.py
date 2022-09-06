# https://www.acmicpc.net/problem/9663

import sys


def attack(x):
    for i in range(x):
        if location[x] == location[i] or abs(location[x] - location[i]) == x - i:
            return False
    return True


def place_queen(x):
    global result 
    
    if x == n:
        result += 1
        return

    for i in range(n):
        location[x] = i
        if attack(x):
            place_queen(x+1)


n = int(sys.stdin.readline())
location = [0] * n
result = 0
place_queen(0)
print(result)