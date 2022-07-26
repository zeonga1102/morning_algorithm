# https://www.acmicpc.net/problem/1110


################################################################
###################### 숫자로 푸는 방법 #########################
################################################################

# num = int(input())

# origin = num
# count = 0
# while True:
#     num = num%10*10 + (num//10 + num%10)%10
#     count += 1

#     if origin == num:
#         print(count)
#         break


################################################################
################## 문자열 이용해서 푸는 방법 #####################
################################################################

num = input()

origin = int(num)
count = 0
while True:
    if int(num) < 10:
        num = num[-1] + num[-1]
    else:
        num = num[1] + str(int(num[0]) + int(num[1]))[-1]

    count += 1
    
    if origin == int(num):
        print(count)
        break