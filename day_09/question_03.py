# https://www.acmicpc.net/problem/1010

def factorial(num):
    if num <= 1:
        return 1

    return num * factorial(num-1)

t = int(input())

for i in range(t):
    n, m = map(int, input().split())

    print(int(factorial(m)/(factorial(n)*factorial(m-n))))