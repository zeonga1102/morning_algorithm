# https://www.acmicpc.net/problem/1157

string = input().upper()

count_letter = [ string.count(chr(ord('A')+i)) for i in range(26) ]

max_ = max(count_letter)

print('?' if count_letter.count(max_) > 1 else chr(ord('A')+count_letter.index(max_)))