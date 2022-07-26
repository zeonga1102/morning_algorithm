# https://www.acmicpc.net/problem/4673


def createSequence(n):
    sequence = []
    for i in range(n):
        result = i

        sum = 0
        for j in range(len(str(i))):
            sum = sum + i // 10**j % 10
        result += sum
            
        if result <= n:    
            sequence.append(result)

    sequence = set(sequence)

    return sequence


def printSelfNumber(n):
    sequence = createSequence(n)
    
    for i in range(1, n+1):
        if not i in sequence:
            print(i)


printSelfNumber(10000)