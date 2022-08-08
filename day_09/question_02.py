# https://www.acmicpc.net/problem/11050

def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num-1)

n, k = map(int, input().split())

print(int(factorial(n)/factorial(k)/factorial(n-k)))