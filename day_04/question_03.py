# https://www.acmicpc.net/problem/4948

# 시간 초과

def make_prime_number_list():
    prime_numbers = []

    for i in range(2, 123456*2+1):
        if i == 2:
            prime_numbers.append(i)
            continue
        
        if i % 2 == 0:
            continue
        
        for j in range(3, int(i**0.5)+1):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    return prime_numbers


prime_numbers = make_prime_number_list()

while True:
    n = int(input())
    
    if n == 0:
        break

    count = 0
    
    for i in range(n+1, 2*n+1):
        if i in prime_numbers:
            count += 1
    
    print(count)