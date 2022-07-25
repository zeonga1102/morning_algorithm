# https://www.acmicpc.net/problem/2588

num1 = int(input())
num2 = int(input())

result = 0
for i in range(3):
    cur = num1*(num2%10)
    print(cur)
    num2 = num2 // 10

    result = result + cur * 10**i

print(result)