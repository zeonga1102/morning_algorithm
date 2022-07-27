# https://www.acmicpc.net/problem/1316

n = int(input())

count = 0
for i in range(n):
    word = input()
    
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            if word[j] in word[j+1:]:
                break
    else:
        count += 1

print(count)