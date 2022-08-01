# https://www.acmicpc.net/problem/2609

a, b = map(int, input().split())

a_list = []
for i in range(1, a+1):
    if a % i == 0:
        a_list.append(i)

b_list = []
for i in range(1, b+1):
    if b % i == 0:
        b_list.append(i)

max_yacsu = max(set(a_list)&set(b_list))

a = a // max_yacsu
b = b // max_yacsu

print(max_yacsu)
print(max_yacsu*a*b)