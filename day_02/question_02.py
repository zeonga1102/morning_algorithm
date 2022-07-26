# https://www.acmicpc.net/problem/4344

##########################################################################
#### sum() 사용 X, 입력한 학생 수와 입력한 점수의 개수가 다를 때 -> 에러 #####
##########################################################################

# c = int(input())

# for i in range(c):
#     list_ = list(map(int, input().split()))

#     sum = 0
#     for j in list_[1:list_[0]+1]:
#         sum += j
#     avg = sum / list_[0]

#     count = 0
#     for j in list_[1:list_[0]+1]:
#         if j > avg:
#             count += 1

#     print(f'{round(count/list_[0]*100, 3):.3f}%')


##########################################################################
##### sum() 사용, 입력한 학생 수와 입력한 점수의 개수가 다를 때 -> 정상 ######
##########################################################################

c = int(input())
for i in range(c):
    students = list(map(int, input().split()))
    avg = sum(students[1:])/students[0]

    count = 0
    for j in students[1:]:
        if j > avg:
            count += 1

    print(f'{round(count/students[0]*100, 3):.3f}%')