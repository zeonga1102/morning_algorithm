# https://www.acmicpc.net/problem/1929

m, n = map(int, input().split())

for i in range(m, n+1):
    if i == 1:
        continue

    if i == 2:
        print(i)
        continue
    
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)