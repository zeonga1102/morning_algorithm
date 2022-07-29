# https://www.acmicpc.net/problem/1037

n = int(input())

list_ = sorted(list(map(int, input().split())))

if n % 2 == 1:
    result = list_[n//2]**2
else:
    result = list_[0] * list_[-1]

print(result)