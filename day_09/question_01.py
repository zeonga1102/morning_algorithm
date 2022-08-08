# https://www.acmicpc.net/problem/1934

# 유클리드 호제법
def GCD(M, N): # 최대공약수
    if N == 0:
        return M
    return GCD(N,M%N)

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(int((a*b)/GCD(a, b)))
