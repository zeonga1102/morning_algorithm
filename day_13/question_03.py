# https://www.acmicpc.net/problem/2798

import sys

n, m = map(int, sys.stdin.readline().split())

cards = [int(i) for i in sys.stdin.readline().split()]
answer = []

for i, v1 in enumerate(cards[:len(cards)-2]):
    for j, v2 in enumerate(cards[i+1:]):
        for k in cards[j+i+2:]:
            cards_sum = v1 + v2 + k
            if cards_sum <= m:
                answer.append(cards_sum)

print(max(answer))