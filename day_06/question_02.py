#https://www.acmicpc.net/source/44712258

t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    
    print(f'{(n-1)%h+1}{(n-1)//h+1:02d}')