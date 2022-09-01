# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter


n = int(sys.stdin.readline())

num_list = []
for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()

print(int(round(sum(num_list)/n)))
print(num_list[len(num_list)//2])

count = Counter(num_list).most_common()
if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(num_list[-1] - num_list[0])